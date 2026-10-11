# Standard Deviation and Coefficient of Variation

> **Part of:** [Statistics](../README.md) · **Previous:** [Variability (Variance)](../06_Variability/) · **Next:** Covariance and Correlation *(to be added)*

Variance tells you how spread out data is, but in squared units that are hard to read. This folder covers the two measures that follow from it:

- **Standard deviation (SD):** the square root of the variance, in the original units.
- **Coefficient of variation (CV):** the SD divided by the mean, with no units, so datasets can be compared.

---

## What's in this folder

| File | Pages | What it is |
|------|:-----:|------------|
| [`01_Standard_Deviation_and_CV_Notes.pdf`](01_Standard_Deviation_and_CV_Notes.pdf) | 7 | Study notes: the concepts, the formulas, a full worked example, Excel and Python commands, and a revision kit. |
| [`02_Standard_Deviation_Data_set_example.pdf`](02_Standard_Deviation_Data_set_example.pdf) | 2 | A clean report of the class workbook: the data set, the results and the step-by-step calculation. |

**Which one to open?**

- **Learning the topic:** start with `01`.
- **Seeing the numbers behind the example:** open `02`.
- **Revising quickly:** use the "30-second revision" box on page 1 and the revision kit on page 6 of `01`.

---

## Overview of each file

### `01_Standard_Deviation_and_CV_Notes.pdf`

| Page | Covers |
|:----:|--------|
| 1 | 30-second revision box · where variance, SD and CV fit together |
| 2 | Standard deviation (definition, sample and population formulas, why it beats variance) · coefficient of variation |
| 3 | The pizza example: the data set, sample vs. population, and the four steps |
| 4 | Squared distances from the mean · results side by side · SD vs. CV chart |
| 5 | Why the CV does not change · reading SD on the data · Excel and Python |
| 6 | Revision kit: formula sheet, six-question self-test with answers, common mistakes |
| 7 | Notes check (three inconsistencies to correct in the class notes) · one-line summary |

The class workbook `02_Standard_Deviation.xlsx` is **attached inside this PDF** on page 3 (stamped "DATA SET SENT"). Open your PDF viewer's Attachments panel or click the file icon to extract it. Some viewers, such as browser previews, do not show attachments.

### `02_Standard_Deviation_Data_set_example.pdf`

| Page | Covers |
|:----:|--------|
| 1 | The data set, the results table, the Excel formulas used, the key finding and a chart of the dollar and peso prices |
| 2 | SD vs. CV chart · step-by-step calculation for both currencies · why the CV stays the same |

The data is shown exactly as in the workbook. The only change is that the sample variances, which the workbook stores as typed text, are recalculated with `=VAR.S`; the values agree.

---

## Quick notes

### Definitions

| | Population | Sample |
|---|---|---|
| Standard deviation | $\sigma = \sqrt{\sigma^2}$ | $s = \sqrt{s^2}$ |
| Coefficient of variation | $CV = \dfrac{\sigma}{\mu}$ | $CV = \dfrac{s}{\bar{x}}$ |

Inside the root, the variance divides by $N$ for a population and by $n-1$ for a sample.

### Why each measure exists

| Measure | Units | Why it is used |
|---|---|---|
| Variance | Squared (dollars²) | Measures spread, but is hard to interpret. |
| Standard deviation | Original (dollars) | Directly interpretable; best for **one** dataset. |
| Coefficient of variation | None | Unit-free; used to **compare** datasets. |

### The pizza example in one table

Ten pizza prices in New York (sample, $n=10$): $1, 2, 3, 3, 5, 6, 7, 8, 9, 11. The same prices are then converted to pesos at 18.81 MXN per dollar.

| Measure | Dollars | Pesos |
|---|:---:|:---:|
| Mean | $ 5.50 | MXN 103.46 |
| Sample variance | $² 10.72 | MXN² 3,793.69 |
| Sample standard deviation | $ 3.27 | MXN 61.59 |
| **Coefficient of variation** | **0.60** | **0.60** |

**Takeaway:** the SDs differ only because the units differ. The CV is 0.60 in both, which shows the two datasets have the **same variability**.

---

## Key takeaways

- **SD = √variance.** It is in the original units, so it is easy to interpret.
- **CV = SD ÷ mean.** It has no units, so it lets you compare datasets on different scales.
- Rescaling data by a factor $c$ multiplies the mean and SD by $c$ and the variance by $c^2$, but **leaves the CV unchanged**.
- Use $n-1$ for a sample and $N$ for a whole population.
- Use the CV only when the mean is clearly above zero.

---

## Notes on the material

- The concepts and numbers come from the class notes and workbook. Some items were added for clarity and are marked as additions in the PDFs: the explanation of why the CV is unchanged, the ±1 SD chart, the self-test and the notes check.
- **Worth correcting in your own class notes:** the notes say "11 restaurants" and also "n = 10" (the workbook has 10 prices; 11 is the highest price); they call 18.81 to 206.91 the exchange rate (it is the price range in pesos, and the rate is 18.81 pesos per dollar); and the variance cells in the workbook are typed text, not formulas.
