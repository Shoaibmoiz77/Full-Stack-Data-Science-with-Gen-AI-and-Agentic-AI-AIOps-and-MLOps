# Measures of Variability: Variance

> **Part of:** [Descriptive Statistics](../README.md) · **Previous:** [Skewness](../05_Skewness/) · **Next:** [Standard Deviation & Coefficient of Variation](../07_Standard_Deviation_and_CV/)

Descriptive statistics describe a dataset with three families of measures. This section covers the third one, **variability**, and its first tool, **variance**.

| # | Family | Question it answers | Covered in |
|---|--------|---------------------|------------|
| 1 | Central tendency | Where is the centre of the data? (mean, median, mode) | [01_Introduction](../01_Introduction_to_statistics/) |
| 2 | Asymmetry | Is the data lopsided? (skewness) | [05_Skewness](../05_Skewness/) |
| 3 | **Variability** | **How spread out is the data?** | **this folder (variance)**, then [07](../07_Standard_Deviation_and_CV/) |

The most common ways to quantify variability are **variance**, **standard deviation** and the **coefficient of variation**.

---

## Table of contents

1. [Learning objectives](#1-learning-objectives)
2. [Sample vs. population](#2-sample-vs-population)
3. [Mean (the reference point)](#3-mean-the-reference-point)
4. [Variance](#4-variance)
5. [Worked example](#5-worked-example)
6. [Why divide by n − 1?](#6-why-divide-by-n--1)
7. [Calculating variance in Excel and Python](#7-calculating-variance-in-excel-and-python)
8. [Key takeaways](#8-key-takeaways)
9. [Slide gallery](#9-slide-gallery)
10. [Files in this folder](#10-files-in-this-folder)

---

## 1. Learning objectives

After working through this section you should be able to:

- Explain what variability means and why a mean alone is not enough to describe data.
- Tell **population** data from **sample** data and choose the right formula for each.
- Write and apply the population variance ($\sigma^2$) and sample variance ($s^2$) formulas.
- Explain why deviations are squared.
- Compute variance by hand, in Excel and in Python.

---

## 2. Sample vs. population

| | Population | Sample |
|---|---|---|
| **Definition** | Every member of the group you care about | A subset drawn from that group |
| **Size symbol** | $N$ | $n$ |
| **Mean symbol** | $\mu$ | $\bar{x}$ |
| **Variance symbol** | $\sigma^2$ | $s^2$ |
| **Nature of the measure** | An exact **parameter** (you are 100% sure of it) | A **statistic**, an approximation of the population parameter |

**Two ideas to remember**

1. The formulas for a sample and a population are different, so always decide which one you have first.
2. A sample gives you only an approximation. **Ten different samples give ten different measures.**

> **Example from the lecture.** The whole United States is the population. California (or Oregon, Michigan, Minnesota, ...) is one sample drawn from it. Computing the same measure on ten different states gives ten different answers, and none of them equals the population value exactly.

---

## 3. Mean (the reference point)

Variance measures spread *around the mean*, so the mean comes first. The two formulas look different but are computed the same way.

$$\text{Population mean: } \mu = \frac{\sum_{i=1}^{N} x_i}{N} \qquad\qquad \text{Sample mean: } \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

---

## 4. Variance

**Definition.** Variance measures the dispersion of a set of data points around their mean.

$$\boxed{\;\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}\;} \qquad \text{(population variance)}$$

$$\boxed{\;s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}\;} \qquad \text{(sample variance)}$$

In words: *take the difference between each observation and the mean, square it, add them all up, then divide by the number of observations (population) or by one less than that (sample).*

**Why square the differences?**
Dispersion is a distance, and a distance cannot be negative. Squaring makes every term non-negative. Without it, deviations above and below the mean would cancel each other out and the total would always be zero.

**Reading the result.** A larger variance means the data points are more spread out around the mean. A variance of 0 means every value is identical.

---

## 5. Worked example

Population data: **1, 2, 3, 4, 5** (so $N = 5$).

**Step 1: Mean**

$$\mu = \frac{1+2+3+4+5}{5} = \frac{15}{5} = 3$$

**Step 2: Squared deviations from the mean**

| $x_i$ | $x_i - \mu$ | $(x_i - \mu)^2$ |
|:-----:|:-----------:|:---------------:|
| 1 | −2 | 4 |
| 2 | −1 | 1 |
| 3 | 0 | 0 |
| 4 | 1 | 1 |
| 5 | 2 | 4 |
| | **Sum** | **10** |

**Step 3a: Population variance** (divide by $N = 5$)

$$\sigma^2 = \frac{(1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2}{5} = \frac{10}{5} = \mathbf{2}$$

**Step 3b: Sample variance** (treat the same five numbers as a *sample* and divide by $n - 1 = 4$)

$$s^2 = \frac{(1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2}{4} = \frac{10}{4} = \mathbf{2.5}$$

The numerator (10) is identical. Only the denominator changes, and that is the whole difference between the two formulas.

| | Denominator | Result |
|---|:-----------:|:------:|
| Population variance $\sigma^2$ | $N = 5$ | **2.00** |
| Sample variance $s^2$ | $n - 1 = 4$ | **2.50** |

> **Note:** the same five numbers can only be "the population" or "a sample" depending on the situation. Whether you divide by $N$ or $n-1$ depends on how the data was collected, not on the numbers themselves.

---

## 6. Why divide by n − 1?

The lecture states the rule: *use $n - 1$ when your data is a sample drawn from a larger population.*

*Supplementary explanation (not in the original lecture):* a sample tends to sit closer to its own mean $\bar{x}$ than to the true population mean $\mu$. Dividing by $n$ would therefore systematically **underestimate** the true spread. Dividing by $n - 1$ (known as **Bessel's correction**) compensates for this, so that $s^2$ is an unbiased estimate of $\sigma^2$. The effect is large for small samples and shrinks as $n$ grows.

---

## 7. Calculating variance in Excel and Python

### Excel

| Goal | Formula |
|---|---|
| Mean | `=AVERAGE(B4:B8)` |
| Population variance | `=VAR.P(B4:B8)` |
| Sample variance | `=VAR.S(B4:B8)` |

These are the exact formulas used in [`02_Variance.xlsx`](02_Variance.xlsx).

### Python

```python
import statistics as st
import numpy as np

data = [1, 2, 3, 4, 5]

# Standard library
st.pvariance(data)   # population variance -> 2
st.variance(data)    # sample variance     -> 2.5

# NumPy: control the denominator with ddof (delta degrees of freedom)
np.var(data)            # ddof=0 (default) -> population variance -> 2.0
np.var(data, ddof=1)    # ddof=1           -> sample variance     -> 2.5
```

> **Common pitfall:** NumPy's `np.var` divides by $N$ by default, whereas pandas' `Series.var()` divides by $n-1$ by default. Always check which one you need.

---

## 8. Key takeaways

- Variability measures **how spread out** data is; the mean alone cannot tell you this.
- **Variance** = the average squared distance of the data points from their mean.
- Population variance divides by $N$; sample variance divides by $n - 1$.
- Differences are **squared** so that they are non-negative and do not cancel out.
- Sample statistics only **approximate** population parameters, so different samples give different results.
- Variance is expressed in **squared units** (for example dollars²), which makes it hard to interpret directly. This is the motivation for [standard deviation](../07_Standard_Deviation_and_CV/), the next topic.

---

## 9. Slide gallery

Screenshots from the lecture, in the order they were presented.

### Sample data vs. population data

| | |
|:--:|:--:|
| ![Different formulas for sample and population](03_Variability_Slides/slide_00.png) | ![Population means 100% sure of the measures](03_Variability_Slides/slide_01.png) |
| **Slide 00.** Sample and population data need different formulas. | **Slide 01.** With population data you are 100% sure of the measures you calculate. |
| ![Sample statistics approximate the population parameter](03_Variability_Slides/slide_02.png) | ![Ten samples give ten different measures](03_Variability_Slides/slide_03.png) |
| **Slide 02.** Sample statistics are an approximation of the population parameter. | **Slide 03.** Ten different samples give ten different measures. |

### Mean and variance formulas

| | |
|:--:|:--:|
| ![Mean formulas](03_Variability_Slides/slide_04.png) | ![Variance concept](03_Variability_Slides/slide_05.png) |
| **Slide 04.** Mean: sample formula (÷ n) and population formula (÷ N). | **Slide 05.** Variance measures dispersion of data points around their mean. |
| ![Variance formulas](03_Variability_Slides/slide_06.png) | |
| **Slide 06.** Population variance $\sigma^2$ and sample variance $s^2$. | |

### Worked example (1, 2, 3, 4, 5)

| | |
|:--:|:--:|
| ![Start by calculating the mean](03_Variability_Slides/slide_07.png) | ![Population variance expanded](03_Variability_Slides/slide_08.png) |
| **Slide 07.** Start with the mean: (1+2+3+4+5)/5 = 3. | **Slide 08.** Plug the mean into the population variance formula. |
| ![Population variance result](03_Variability_Slides/slide_09.png) | ![Sample variance uses n minus 1](03_Variability_Slides/slide_10.png) |
| **Slide 09.** Divide by N = 5, giving a population variance of 2.00. | **Slide 10.** For a sample, the denominator becomes n − 1 = 4, giving 2.50. |

---

## 10. Files in this folder

```text
06_Variability/
├── README.md                          <- this document (cleaned-up, readable version of the lecture)
├── 01_Variability_Class_Notes.txt     <- original raw class notes
├── 02_Variance.xlsx                   <- Excel worked example
└── 03_Variability_Slides/             <- 11 lecture slide screenshots
    └── slide_00.png ... slide_10.png
```

| File | Description |
|---|---|
| [`01_Variability_Class_Notes.txt`](01_Variability_Class_Notes.txt) | Original class notes, kept unedited for reference. |
| [`02_Variance.xlsx`](02_Variance.xlsx) | One sheet, **Variance**. Population `1, 2, 3, 4, 5` with live formulas for the mean (3), population variance (2) and sample variance (2.5). It also holds a second column labelled "Imaginary population" (`1, 1, 1, 2, 3, 4, 5, 5, 5, 5`) that no formula uses. |
| [`03_Variability_Slides/`](03_Variability_Slides/) | Lecture slides used in the gallery above. |

---

**Next up:** [Standard Deviation & Coefficient of Variation](../07_Standard_Deviation_and_CV/), which fixes the "squared units" problem of variance and lets you compare spread across datasets.

