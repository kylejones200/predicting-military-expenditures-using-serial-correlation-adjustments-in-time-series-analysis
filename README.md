# Predicting Military Expenditures using Serial Correlation Adjustments in Time Series Analysis

Published: 2025-03-09
Medium: [https://medium.com/@kyle-t-jones/predicting-military-expenditures-using-serial-correlation-adjustments-in-time-series-analysis-2b4b3df790b0](https://medium.com/@kyle-t-jones/predicting-military-expenditures-using-serial-correlation-adjustments-in-time-series-analysis-2b4b3df790b0)

## Business context

Military expenditures are a key indicator of national capability and strategic priorities. Understanding the factors influencing military spending is crucial for researchers analyzing defense policies and international relations. This study examines the relationship between military expenditures (milex) and two primary predictors: iron and steel production (irst) and energy consumption (pec).

We expect serial correlation in the residuals because this is time series data. So there is potential that OLS will lead to inefficient standard errors and misleading statistical inferences. We will look at the data in three ways: estimating an Ordinary Least Squares (OLS) regression, correcting for serial correlation using Newey-West standard errors, and differencing the data to determine whether Newey-West corrections remain necessary.

I am using the National Material Capabilities (NMC) dataset (Version 6.0), which covers military and industrial indicators for countries from 1816 to 2016. Key variables include:

## About

Place the code for this article in this repository.
The original article export is saved as `article.md`.

## Files

Add your `.ipynb`, `.py`, `.yaml`, `.js`, `.ts`, or other project files here.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).