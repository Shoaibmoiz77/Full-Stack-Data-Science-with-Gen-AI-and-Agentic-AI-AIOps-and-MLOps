# =============================================================================
# DATA PREPROCESSING WITH SCIKIT-LEARN
# =============================================================================
# Goal: turn the raw Data.csv into clean numeric arrays that a machine
# learning model can learn from.
#
# Steps:
#   1. Import libraries and load the dataset
#   2. Separate independent variables (X) from the dependent variable (y)
#   3. Fill in missing numerical values        (SimpleImputer)
#   4. Convert categorical text to numbers      (LabelEncoder)
#   5. Split into training and testing sets     (train_test_split)
#   6. Scale the features                       (StandardScaler)
# =============================================================================


# -----------------------------------------------------------------------------
# 1. IMPORT LIBRARIES
# -----------------------------------------------------------------------------
import numpy as np                  # arrays and numerical operations
import matplotlib.pyplot as plt     # plotting (not used yet in this script)
import pandas as pd                 # reading and handling tabular data


# -----------------------------------------------------------------------------
# 2. IMPORT THE DATASET AND SEPARATE X AND y
# -----------------------------------------------------------------------------
# Read the CSV file into a DataFrame.
# The "r" prefix makes it a raw string so the backslashes in a Windows path
# are not treated as escape characters.
dataset = pd.read_csv(r"C:\Users\shoai\Downloads\Data.csv")

# INDEPENDENT VARIABLES (X): the inputs the model learns from.
# iloc[rows, columns] -> ":" takes all rows, ":-1" takes every column except
# the last one. ".values" converts the result to a NumPy array.
x = dataset.iloc[:, :-1].values

# DEPENDENT VARIABLE (y): the target the model must predict.
# Column index 3 is the last column (Purchased).
y = dataset.iloc[:, 3].values


# -----------------------------------------------------------------------------
# 3. HANDLE MISSING NUMERICAL VALUES
# -----------------------------------------------------------------------------
# Most models cannot work with empty (NaN) cells, so they are filled in first.
from sklearn.impute import SimpleImputer

# By default SimpleImputer replaces each missing value with the MEAN of its
# column.
imputer = SimpleImputer()

# fit(): learn the mean of each column.
# Columns 1 and 2 (Age and Salary) are the numerical ones; the slice 1:3
# stops before index 3. Column 0 (text) is left out because a mean cannot be
# computed for text.
imputer = imputer.fit(x[:, 1:3])

# transform(): replace the missing values with the means learned above and
# write the completed columns back into x.
x[:, 1:3] = imputer.transform(x[:, 1:3])


# -----------------------------------------------------------------------------
# 4. ENCODE CATEGORICAL DATA
# -----------------------------------------------------------------------------
# Models work with numbers, not text, so category labels become integers.
from sklearn.preprocessing import LabelEncoder

# --- Independent variable: column 0 (the text column, State) ---
labelencoder_x = LabelEncoder()

# This call only previews the encoding; its result is not stored anywhere.
# The next line does the real work, so this line could be removed.
labelencoder_x.fit_transform(x[:, 0])

# fit_transform(): learn the categories, then replace each one with an
# integer (assigned alphabetically: 0, 1, 2, ...) and store it back in x.
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

# --- Dependent variable: y (Yes / No) ---
# A separate encoder is used because y has its own set of categories.
# Alphabetically No -> 0 and Yes -> 1.
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# -----------------------------------------------------------------------------
# 5. SPLIT THE DATA INTO TRAINING SET AND TEST SET
# -----------------------------------------------------------------------------
# The model learns from the training set and is then judged on the test set,
# data it has never seen, to check that it works on new data.
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.2,    # 20% test, 80% train
                                                    random_state=0)   # fixed seed: same split every run


# -----------------------------------------------------------------------------
# 6. FEATURE SCALING
# -----------------------------------------------------------------------------
# Features such as Age (tens) and Salary (tens of thousands) sit on very
# different scales. StandardScaler rescales each column to mean 0 and
# standard deviation 1 (z = (value - mean) / std), so no column dominates just
# because its numbers are larger.
from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()

# Training set: learn the mean and std from the training data, then scale it.
x_train = sc_x.fit_transform(x_train)

# Test set: only transform, reusing the training mean and std. Fitting on the
# test set would leak information from the test data into preprocessing.
x_test = sc_x.transform(x_test)
