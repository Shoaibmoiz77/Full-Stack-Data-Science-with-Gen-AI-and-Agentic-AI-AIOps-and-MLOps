# Exploratory Data Analysis (EDA) & Machine Learning — Structured Notes

## 1. What is EDA?

EDA is the process of converting **raw data → clean data**, so it becomes usable for building a machine learning model. It is done through **7 core techniques**, applied roughly in this order:

| # | Technique | Purpose |
|---|-----------|---------|
| 1 | Variable Identification | Classify each column as dependent/independent, relevant/irrelevant |
| 2 | Univariate Analysis | Study one variable at a time |
| 3 | Bivariate Analysis | Study the relationship between two variables |
| 4 | Outlier Treatment | Detect and handle extreme/abnormal values |
| 5 | Missing Value Treatment | Detect and handle nulls/blanks |
| 6 | Variable Transformation | Convert variables into a more model-friendly form |
| 7 | Variable Creation | Engineer new features from existing ones |

---

## 2. Variable Identification

**Terminology mapping:**

| Business term | Data term |
|---|---|
| Excel sheet | Dataset |
| Column | Attribute / Variable |

**Example — a family of 4 as a dataset:**

| Member | Role | Variable Type |
|---|---|---|
| Father | Govt. employee — pays house EMI, kids' fees, land loan | **Dependent variable (Y)** |
| Mother | Housewife | Independent variable (X1) |
| Brother | 4th grade student | Independent variable (X2) |
| Sister | 3rd grade student | Independent variable (X3) |

This maps to the equation of **Multiple Linear Regression**:

$$Y = X_1 + X_2 + X_3$$

**Key definitions:**
- **Dependent variable (Y)** = target attribute = the variable being predicted
- **Independent variable (X)** = non-target attribute(s) = the variable(s) used to predict Y

**Relevance matters:** every attribute must be checked for relevance before modeling.
- If a model is built using **irrelevant attributes**, it causes **multicollinearity**, which leads to **overfitting**.
- An overfit model has **poor accuracy and high error**, and cannot reliably be deployed.
- Business impact: a flawed model → product/website can't be shipped → potential business loss.

*(Note: strictly speaking, multicollinearity — redundancy among independent variables — is one specific cause of a poor model; it isn't identical to overfitting, but including irrelevant/noisy features is a common contributor to overfitting in general.)*

---

## 3. Types of Machine Learning Problems (based on Y)

| Type | Condition on Dependent Variable (Y) | Example |
|---|---|---|
| **Regression** | Y is a **continuous** variable | Predicting gold price |
| **Classification** | Y is **binary/categorical** | Win vs. Loss |
| **Clustering** | **No dependent variable** — used for grouping discrete/unlabeled data | Segmenting students by score range |

---

## 4. Understanding Data Types

| Data Type | Description | Examples |
|---|---|---|
| **Continuous** | Keeps increasing/decreasing across a range, no fixed stopping point | Gold price, petrol price, electricity bill, EV car sales, stock price, house price, land price, weather |
| **Binary** | Only two possible outcomes | Win/Loss, Profit/Loss, Positive/Negative |
| **Discrete** | Has a fixed, finite stopping point/scale | Student exam score (capped at 100) |

---

## 5. Regression Algorithms (used when Y is continuous)

1. Simple Linear Regression
2. Multiple Linear Regression
3. Gradient Descent — Stochastic Gradient Descent (SGD) / Batch Gradient Descent
4. Regularization: **L1 (Lasso Regression)**, **L2 (Ridge Regression)**
5. K-Nearest Neighbors (KNN) Regressor
6. Decision Tree Regression
7. Random Forest Regression
8. XGBoost Regression
9. LightGBM (LGBM) Regression
10. Artificial Neural Network (ANN) Regression
11. Time Series Regression
12. Support Vector Regressor (SVR)

---

## 6. Classification Algorithms (used when Y is binary/categorical)

1. Logistic Regression
2. Support Vector Machine (SVM)
3. KNN Classifier
4. Decision Tree Classifier
5. Naive Bayes Classifier
6. Random Forest Classifier
7. XGBoost (Extreme Gradient Boosting) Classifier
8. LightGBM (LGBM) Classifier
9. Artificial Neural Network (ANN) Classifier

---

## 7. Clustering Algorithms (used for grouping, no Y)

1. Principal Component Analysis (PCA) — *dimensionality reduction, often used alongside clustering*
2. K-Means
3. Hierarchical Clustering
4. DBSCAN

**Worked example — clustering student scores into 5 groups:**

| Group | Score Range | Interpretation |
|---|---|---|
| 1 | > 95% | Top rank students |
| 2 | 90% – 97% | High performers |
| 3 | 80% – 90% | Above average |
| 4 | 70% – 80% | Average |
| 5 | 30% – 60% | Needs improvement |

*(Overlap between groups 1 and 2 in the original ranges is worth tightening in practice — e.g., >95%, 90–95%, 80–90%, 70–80%, 30–60% — so bins don't overlap.)*

Clustering like this can help identify the **best candidates** from a discrete/ungrouped dataset.

---

## 8. Where Statistics Fits In

Once a regression or classification model is built, statistics is used to **test whether the model is accurate**.

**Regression performance metrics:**
- R² (R-squared)
- Adjusted R²
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

**Classification performance metric:**
- Confusion Matrix (and metrics derived from it: accuracy, precision, recall, F1-score)

---

## 9. Variable Identification — Deeper Dive

- **Dependent Variable (DV):** always exactly **1** (Y)
- **Independent Variable (IV):** can be **many** (X1, X2, X3, …)
- Attributes must be sorted into:
  - **Relevant attributes** — keep
  - **Non-relevant attributes** — drop

**Why this matters in the ML pipeline/workflow:**
Selecting the right relevant attributes is the **first and most important step** to achieving good model accuracy. Irrelevant attributes → multicollinearity / overfitting → poor accuracy → high error → model not deployable.

---

## 10. Univariate Analysis

- Definition: plotting/analyzing **1 variable at a time**.
- Goal: understand the distribution, spread, and central tendency of a single attribute (e.g., histogram, box plot for a single column).

---

## 11. Bivariate Analysis

- Definition: plotting/analyzing the relationship between **2 variables** at a time.
- Central concept: **Correlation** — the relationship/association between two attributes.

**Types of correlation:**

| Correlation Type | Range | Meaning |
|---|---|---|
| Positive correlation | 0 to +1 | As one variable increases, the other also increases |
| Negative correlation | -1 to 0 | As one variable increases, the other decreases |
| No correlation | 0 | No relationship between the variables |

**Overall correlation coefficient range:** **-1 to +1**

---

## Quick-Reference Summary

```
RAW DATA
   │
   ▼
[EDA — 7 Steps]
1. Variable Identification
2. Univariate Analysis
3. Bivariate Analysis
4. Outlier Treatment
5. Missing Value Treatment
6. Variable Transformation
7. Variable Creation
   │
   ▼
CLEAN DATA
   │
   ▼
[Choose ML Problem Type based on Y]
├── Y continuous     → Regression
├── Y binary/category → Classification
└── No Y (discrete)   → Clustering
   │
   ▼
[Build Model] → [Evaluate with Stats: R², RMSE, Confusion Matrix, etc.]
```

---

### Notes on gaps in the original material
Steps 4–7 (Outlier Treatment, Missing Value Treatment, Variable Transformation, Variable Creation) were listed as part of the 7-step EDA framework but not detailed in your raw notes. Worth filling in next as a follow-up:
- **Outlier Treatment:** IQR method, Z-score method, capping/flooring
- **Missing Value Treatment:** mean/median/mode imputation, KNN imputation, dropping rows/columns
- **Variable Transformation:** log transform, scaling (normalization/standardization), encoding categorical variables
- **Variable Creation:** feature engineering — deriving new columns from existing ones (e.g., extracting "day of week" from a date)
