#
# Because I always forget these equations and
# never want to look them up again...
#

#
# load useful libraries
#
from numpy import pi
from config.precision_config import float_tse

def frequency_in_hertz_to_period_in_seconds(frequency : float_tse) -> float_tse:
    return 1. / frequency

def period_in_seconds_to_frequency_in_hertz(period : float_tse) -> float_tse:
    return 1. / period
