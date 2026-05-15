# Description: Short example for Predicting Military Expenditures using Serial Correlation Adjustments in Time Series Analysis.


import logging

import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_breusch_godfrey


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


    df = df[["milex", "irst", "pec"]].dropna()
    # Define dependent and independent variables
    Y = df["milex"]
    X = df[["irst", "pec"]]
    X = sm.add_constant(X)
    # Fit OLS model
    ols_model = sm.OLS(Y, X).fit()
    logger.info(ols_model.summary())

    lm_test = acorr_breusch_godfrey(ols_model, nlags=3)
    lm_stat, lm_pvalue, f_stat, f_pvalue = lm_test
    logger.info(f"LM Statistic: {lm_stat:.4f}, p-value: {lm_pvalue:.4f}")

    # LM Statistic: 14374.4550, p-value: 0.0000

    nw_model = ols_model.get_robustcov_results(cov_type="HAC", maxlags=3)
    logger.info(nw_model.summary())

    # Apply differencing
    df["milex_diff"] = df["milex"].diff()
    df = df.dropna()

    # Fit OLS on differenced data
    Y_diff = df["milex_diff"]
    X_diff = df[["irst", "pec"]]
    X_diff = sm.add_constant(X_diff)
    ols_diff_model = sm.OLS(Y_diff, X_diff).fit()
    logger.info(ols_diff_model.summary())

    lm_test_diff = acorr_breusch_godfrey(ols_diff_model, nlags=3)
    logger.info(
        f"LM Statistic (Differenced): {lm_test_diff[0]:.4f}, p-value: {lm_test_diff[1]:.4f}"
    )

    # LM Statistic (Differenced): 91.2065, p-value: 0.0000

    nw_diff_model = ols_diff_model.get_robustcov_results(cov_type="HAC", maxlags=3)
    logger.info(nw_diff_model.summary())


if __name__ == "__main__":
    main()
