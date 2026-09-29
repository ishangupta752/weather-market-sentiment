"""Illustrative regression templates for the paper's empirical design."""
import statsmodels.formula.api as smf

def fit_return_model(df):
    formula = "excess_return ~ cloud + rain + temp + sun + mkt_rf + smb + hml + rmw + cma + C(city) + C(month)"
    return smf.ols(formula, data=df).fit()

def fit_volume_model(df):
    formula = "delta_log_volume ~ cloud + rain + temp + sun + mkt_rf + smb + hml + rmw + cma + C(city) + C(month)"
    return smf.ols(formula, data=df).fit()
