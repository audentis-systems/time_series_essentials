import numpy as np
from statsmodels.tsa.stattools import adfuller

from .config.precision_config import float_tse, int_tse

def compute_verbose_adf_dict(
    time_series : np.array,
    p_value_cutoff : float_tse = 0.05,
    autolag : str = 'AIC',
) -> dict:

    # 
    # move this to a separate library
    #
    def interpret_adf_results(reject_null):
        if reject_null:
            return "Reject the null hypothesis (H0). The time series is likely stationary."
        else:
            return "Fail to reject the null hypothesis (H0). The time series is likely non-stationary (has a unit root)."
                
    adf_result = adfuller(time_series, autolag = autolag)
    reject_null = adf_result[1] <= p_value_cutoff    
    
    adf_result_dict = {
        'what' : 'Augmented Dickey-Fuller Test Results',
        'ADF_statistic' : float_tse(adf_result[0]),
        'p_value' : float_tse(adf_result[1]),
        'lags_used' : int_tse(adf_result[2]),
        'n' : int_tse(adf_result[3]),
        'reject_null' : reject_null,
        'interpretation' : interpret_adf_results(reject_null),
        'critical_values' : {}
    }

    for key, value in adf_result[4].items():
        adf_result_dict['critical_values'][key] =  float_tse(value)

    return adf_result_dict
