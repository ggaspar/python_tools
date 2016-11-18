
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

def smart_cast(int_str,default_value=0):
    try:
        return int(int_str)
    except:
        return default_value
