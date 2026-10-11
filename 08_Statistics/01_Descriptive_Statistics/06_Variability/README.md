# Measures of Variability: Variance

> **Part of:** [Statistics](../README.md) · **Previous:** [Skewness](../05_Skewness/) · **Next:** Standard Deviation & Coefficient of Variation *(to be added)*

Descriptive statistics summarise a dataset with three families of measures. This folder covers the third family, **variability**, and its first tool, **variance**: a single number that says how spread out the data is around its mean.

| # | Family | Question it answers | Where |
|---|--------|---------------------|-------|
| 1 | Central tendency | Where is the centre of the data? (mean, median, mode) | [01_Introduction_to_statistics](../01_Introduction_to_statistics/) |
| 2 | Asymmetry | Is the data lopsided? (skewness) | [05_Skewness](../05_Skewness/) |
| 3 | **Variability** | **How spread out is the data?** | **this folder** |

---

## Contents of this folder

| File | Type | Pages | What it is |
|------|------|:-----:|------------|
| [`01_Variability_Notes.pdf`](01_Variability_Notes.pdf) | Study notes (portrait) | 5 | A structured written explanation of variance with formulas, a worked example, a comparison of datasets, Excel and Python code, practice problems and a summary. |
| [`02_Variability_Class_Notes_(worked_examples).pdf`](02_Variability_Class_Notes_%28worked_examples%29.pdf) | Illustrated lecture slides (landscape) | 14 | The 11 lecture slides, each shown beside a plain-language explanation, plus the full worked example, the spreadsheet figures and a one-page cheat sheet. |

**Which one should I open?**

- **Learning the topic from scratch:** read `01` first, then go through `02` to see the same ideas on the original slides.
- **Revising before an exam or interview:** go straight to page 14 of `02` (the cheat sheet) and the practice problems at the end of `01`.
- **Following the lecture:** use `02`, which keeps the slides in lecture order.

### What each PDF covers

**`01_Variability_Notes.pdf`**

| Page | Sections |
|:----:|----------|
| 1 | At-a-glance summary · where variability fits · population vs. sample |
| 2 | The mean · the variance formulas · the four calculation steps · why differences are squared |
| 3 | Worked example on 1, 2, 3, 4, 5 (population and sample variance) |
| 4 | Comparing the spread of three datasets · why divide by *n* − 1 · Excel formulas |
| 5 | Python code · common pitfall · practice problems with answers · summary |

**`02_Variability_Class_Notes_(worked_examples).pdf`**

| Pages | Part | Lecture slides |
|:-----:|------|:--------------:|
| 1 | Cover and roadmap | none |
| 2–5 | **A.** Sample vs. population | 1–4 |
| 6–8 | **B.** Mean and variance | 5–7 |
| 9–12 | **C.** Worked example, step by step | 8–11 |
| 13 | The Excel workbook behind the lecture, reproduced with its formulas | none |
| 14 | Cheat sheet: formulas, six steps, Excel/Python commands, common mistakes | none |

---

## Concepts at a glance

### Population vs. sample

| | Population | Sample |
|---|---|---|
| Meaning | Every member of the group | A subset of the group |
| Size | $N$ | $n$ |
| Mean | $\mu$ | $\bar{x}$ |
| Variance | $\sigma^2$ | $s^2$ |
| Nature | Exact **parameter** | **Statistic**, an approximation of the parameter |

Different samples from the same population give different results, so a sample statistic only approximates the population value.

### The formulas

$$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} \qquad \text{(population variance)}$$

$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1} \qquad \text{(sample variance)}$$

Each difference from the mean is **squared** so that it is non-negative. Without squaring, values above and below the mean would cancel and the total would always be 0.

### Worked example

Data: **1, 2, 3, 4, 5**. The mean is 3, and the squared deviations are 4, 1, 0, 1, 4, which sum to **10**.

| | Calculation | Result |
|---|:---:|:---:|
| Population variance $\sigma^2$ | $10 \div N = 10 \div 5$ | **2** |
| Sample variance $s^2$ | $10 \div (n-1) = 10 \div 4$ | **2.5** |

The numerator is the same. Only the denominator changes.

### Excel and Python

| Tool | Population (÷ *N*) | Sample (÷ *n* − 1) |
|------|--------------------|--------------------|
| Excel | `=VAR.P(range)` | `=VAR.S(range)` |
| Python `statistics` | `pvariance(data)` | `variance(data)` |
| NumPy | `np.var(data)` | `np.var(data, ddof=1)` |
| pandas | `Series.var(ddof=0)` | `Series.var()` |

> **Pitfall:** NumPy divides by *N* by default, while pandas divides by *n* − 1 by default.

---

## Key takeaways

- Variability describes **how spread out** data is. A mean alone cannot show this.
- **Variance** is the average squared distance of the data points from their mean.
- Use **N** for a whole population and **n − 1** for a sample.
- Variance is measured in **squared units** (for example dollars²), which makes it hard to interpret directly. The next topic, standard deviation, takes the square root to fix this.

---

## Notes on the material

- The lecture slides and the worked numbers (mean 3, population variance 2, sample variance 2.5) come from the class.
- A few items were added for clarity and are not from the lecture: the sampling table on slide 4 of the slide deck (all 10 samples of size 3 from 1–5), the comparison of three datasets and the *n* − 1 explanation in the notes, the practice problems and the cheat sheet. The sampling table, the *n* − 1 explanation and the extra sections in the notes are marked as additions inside the PDFs; the cheat sheet summarises the same material.
- The Excel workbook used in class is reproduced on page 13 of `02` but is not stored in this folder.
