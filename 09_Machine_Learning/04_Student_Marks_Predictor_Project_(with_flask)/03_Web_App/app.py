# -*- coding: utf-8 -*-
"""
Student Mark Predictor - Flask web app (the "front end").

What this file does
-------------------
1. Loads the trained model that was saved earlier as a .pkl file (see 01_Model_Training).
2. Shows a web page with one box: "study hours".
3. When the user presses the button, sends the hours to the model and shows the predicted marks.
4. Writes every (hours, prediction) pair to a CSV log file.

Run it from this folder:   python app.py      then open  http://127.0.0.1:5000
"""

from pathlib import Path

import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template

# ---------------------------------------------------------------------------
# Paths (relative to this file, so the project works on any computer)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

# The saved model lives in its own folder: ../02_Saved_Model
# It is created by the notebook in 01_Model_Training (see the README).
MODEL_PATH = BASE_DIR.parent / "02_Saved_Model" / "student_mark_predictor.pkl"

# Every prediction made through the web page is logged here.
LOG_PATH = BASE_DIR / "smp_data_from_app.csv"

# ---------------------------------------------------------------------------
# Start the app and load the model ONCE, when the server starts
# ---------------------------------------------------------------------------
app = Flask(__name__)                 # looks for ./templates and ./static next to this file
model = joblib.load(MODEL_PATH)       # the trained Simple Linear Regression model

df = pd.DataFrame()                   # in-memory table of predictions made since the server started


# ---------------------------------------------------------------------------
# Route 1: the home page  (opened with a normal GET request)
# ---------------------------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')          # shows the empty form


# ---------------------------------------------------------------------------
# Route 2: the prediction  (the form sends its data here with POST)
# ---------------------------------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    global df

    # 1) Read what the user typed. The form has a single field named "study_hours".
    #    request.form.values() gives text, so int() turns it into a whole number.
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)

    # 2) Reject impossible values (a day has only 24 hours).
    #    Note: this check lets 0 through, although the message below says "1 to 24".
    if input_features[0] < 0 or input_features[0] > 24:
        return render_template(
            'index.html',
            prediction_text='Please enter valid hours between 1 to 24 if you live on the Earth')

    # 3) Ask the model for a prediction.
    #    model.predict expects a 2-D input, so the hours are wrapped in a list.
    #    The answer is also 2-D: [0][0] picks the single number, .round(2) keeps two decimals.
    output = model.predict([features_value])[0][0].round(2)

    # 4) Remember this prediction and save all of them to the CSV log.
    df = pd.concat(
        [df, pd.DataFrame({'Study Hours': input_features, 'Predicted Output': [output]})],
        ignore_index=True)
    print(df)
    df.to_csv(LOG_PATH)

    # 5) Show the page again with the answer filled in ({{ prediction_text }} in index.html).
    return render_template(
        'index.html',
        prediction_text='You will get [{}%] marks, when you do study [{}] hours per day '.format(
            output, int(features_value[0])))


if __name__ == "__main__":
    app.run(host='127.0.0.1')         # development server, this computer only, port 5000

    # To make the app reachable from other computers on the network, use instead:
    # app.run(host='0.0.0.0', port=8080)
