# Inferential Statistics

In-depth notes on inferential statistics, from scratch-level basics to common hypothesis tests. Study the folders in order: each topic builds on the one before and ends with a summary and practice questions with answers.

| # | Folder | What you learn |
|---|--------|----------------|
| 00 | [`00_Introduction_and_course_notes`](./00_Introduction_and_course_notes/) | Original course summary PDF |
| 01 | [`01_Foundations`](./01_Foundations/) | Population, sample, parameter, statistic, data types, sampling methods and bias, and the logic of inference. |
| 02 | [`02_Probability_Basics`](./02_Probability_Basics/) | The language of chance that every later topic relies on. |
| 03 | [`03_Probability_Distributions`](./03_Probability_Distributions/) | What a distribution is, and the families used throughout inference. |
| 04 | [`04_Normal_Distribution_and_Standardization`](./04_Normal_Distribution_and_Standardization/) | The bell curve, z-scores and the z-table. |
| 05 | [`05_Sampling_Distributions`](./05_Sampling_Distributions/) | Why a statistic varies, and exactly how the sample mean and proportion behave. |
| 06 | [`06_Central_Limit_Theorem`](./06_Central_Limit_Theorem/) | Why averages become normal whatever the population looks like. |
| 07 | [`07_Standard_Error`](./07_Standard_Error/) | Measuring the precision of a sample statistic. |
| 08 | [`08_Point_Estimation`](./08_Point_Estimation/) | Estimators and estimates, and why one number is not enough. |
| 09 | [`09_Confidence_Intervals`](./09_Confidence_Intervals/) | From a point estimate to a range of plausible values. |
| 10 | [`10_Hypothesis_Testing`](./10_Hypothesis_Testing/) | Deciding between two claims with data. |
| 11 | [`11_Common_Tests_and_Choosing_One`](./11_Common_Tests_and_Choosing_One/) | The standard tests and how to pick the right one. |
| 12 | [`12_Type_I_and_Type_II_Errors`](./12_Type_I_and_Type_II_Errors/) | The two ways a hypothesis test can be wrong, and test power. |
| 13 | [`13_P_Value`](./13_P_Value/) | The smallest significance level at which the null can be rejected. |

## Learning path

```text
Foundations -> Probability -> Distributions -> Normal curve -> Sampling distributions
   -> Central Limit Theorem -> Standard error -> Point estimation
   -> Confidence intervals -> Hypothesis testing -> Common tests
   -> Type I and II errors -> P-value
```

## Prerequisites

Descriptive statistics (mean, median, standard deviation, correlation): see [`../01_Descriptive_Statistics/`](../01_Descriptive_Statistics/).

## Tools used in the Python snippets

`numpy` and `scipy` (`pip install numpy scipy`).
