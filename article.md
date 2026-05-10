# Predicting Military Expenditures using Serial Correlation Adjustments in Time Series Analysis Military expenditures are a key indicator of national capability and
strategic priorities. Understanding the factors influencing military...

### **Predicting Military Expenditures using Serial Correlation Adjustments in Time Series Analysis** 

Military expenditures are a key indicator of national capability and strategic priorities. Understanding the factors influencing military spending is crucial for researchers analyzing defense policies and international relations. This study examines the relationship between military expenditures (milex) and two primary predictors: iron and steel production (irst) and energy consumption (pec).

We expect serial correlation in the residuals because this is time series data. So there is potential that OLS will lead to inefficient standard errors and misleading statistical inferences. We will look at the data in three ways: estimating an Ordinary Least Squares (OLS) regression, correcting for serial correlation using Newey-West standard errors, and differencing the data to determine whether Newey-West corrections remain necessary.

### **Dataset Description**
I am using the National Material Capabilities (NMC) dataset (Version 6.0), which covers military and industrial indicators for countries from 1816 to 2016. Key variables include:

- milex: Military Expenditures (in thousands of current-year British Pounds until 1913, and in US Dollars thereafter)
- irst: Iron and steel production (thousands of tons)
- pec: Primary energy consumption (thousands of coal-ton equivalents)
- year: Year of observation
- ccode: Correlates of War (COW) country code
- stateabb: Three-letter country abbreviation

As a matter of policy policy, military expenditures tend to be correlated from year to year. I suspect there will be serial correlation in residuals and ancicipate needed to make statistical adjustments to get robust predictions.

### **OLS Regression: Baseline Model**
We start by estimating a standard Ordinary Least Squares (OLS) regression


where milex_t represents military expenditures, and ϵt is the error term.



#### **Breusch-Godfrey LM Test for Serial Correlation**
To determine whether serial correlation exists, we conduct the Breusch-Godfrey LM test:



Results: The test confirms serial correlation (p-value = 0.000). We need to apply a correction.

### **Correcting for Serial Correlation: Newey-West Standard Errors**
To address the issue of autocorrelated residuals, we apply Newey-West standard errors, which adjust for heteroskedasticity and autocorrelation:



Newey-West adjustments provide robust standard errors. This reduces bias in hypothesis testing.

### **Testing Differencing: Does Serial Correlation Persist?**
To check whether differencing eliminates serial correlation, we transform milex into first differences:




We then repeat the Breusch-Godfrey test to assess whether serial correlation persists.



If the differenced series no longer exhibits serial correlation, standard OLS results become valid. If serial correlation persists, Newey-West remains necessary.

Finally, we apply Newey-West standard errors to the differenced model:



### **Results and Discussion**
Initial OLS regression showed serial correlation as confirmed by the LM test (p-value = 0.000). We applied the Newey-West standard errors corrected for autocorrelation to improve the reliability of standard errors.

Differencing the military expenditure data reduced serial correlation, but the LM test on the differenced model showed some remaining autocorrelation. The coefficients in the differenced OLS are not statistically significant. The R-squared also drops from .723 to .011. This study shows the importance of addressing serial correlation when modeling time series data. The standard OLS model had from serial correlation and we needed to adjust the standard errors with Newey-West. While differencing the data reduced the autocorrelation, residual effects remained, confirming the necessity of robust standard errors.

Another approach would be to explore this data using time series models like as ARIMA or VAR.

Plots for US military expendiutre. The dataset has expendure data on 217 countries. Let's look at just the US.

We see an increase in millitary expenditure around 1918--1920 (WWI) and 1940--1945 (WWII). From 1950 to present we see a large increase in expenditure.


The autocorrelation shows that the first 7 lags are statistically significant.


<figcaption>\</figcaption>


Even after we differenced the data, this plot shows that we have autocorrelation for lags 8, 9, 10, and 11.


This plot shows us actual expenditure (black) and year over year differenced expenditure (grey).
