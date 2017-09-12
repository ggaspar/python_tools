import sqlalchemy as sqlalc
from dashboard_de.models import dataAdministration
from dashboard_de.tools_date import get_previous_monday, get_days_of_month, get_list_of_months, get_quarter_fy, get_list_of_weeks, get_fy_limits, get_list_of_mondays, get_list_of_days, get_list_of_quarters
from dashboard_de.tools_data_structures import get_clean_limit_dates, get_categories
import datetime as dt
from dashboard_de.consts import *




def smart_cast(int_str,default_value=0):
    try:
        return int(int_str)
    except:
        return default_value


def rolling_mean(list, window):
    list_of_means = []
    real_window = window
    for index,value in enumerate(list):
        if value == 0:
            real_window = real_window + 1
        else:
            real_window = window

        start_point = 0 if index < real_window else index + 1 - real_window
        windowed_list = list[start_point : index + 1]
        cleaned_list = [i for i in windowed_list if i > 0]
        if len(cleaned_list) == 0:
            mean = 0
        else:
            mean = sum(cleaned_list) / len(cleaned_list)
        list_of_means.append(mean)
    return list_of_means


def standard_round(number, decimal_numbers = 0):
    """because python uses the banker round, which is not always easy to explain :)"""
    import decimal
    rounding_mask = "1." + "".join(["0" for n in range(decimal_numbers)])
    return float(decimal.Decimal(number)\
                 .quantize(decimal.Decimal(rounding_mask.strip(".")), rounding=decimal.ROUND_HALF_UP))

def stringuify_number(number):
    number = int(number)
    MILLION = 1000000.0
    THOUSAND = 1000.0
    millions = round(number / MILLION,1)
    thousands = round((number % MILLION) / THOUSAND, 1)

    if millions >= 1:
        result = "{0}M".format(str(millions).strip('0').strip('.'))
    elif thousands >= 1:
        result = "{0}K".format(str(thousands).strip('0').strip('.'))
    else:
        result = "{0}".format(number)
    return result

def get_percentage(base, total, rounding=0):

    percentage = 0 if total == 0 or total is None else \
            round(float(base or 0) * 100 / float(total), rounding)
    percentage = int(percentage) if rounding is 0 else percentage
    return percentage




