import datetime as dt
import calendar


def delta_months(date, number_of_months):
    """timedelta doesn't do months delta..."""
    if number_of_months is 0:
        return date
    absolute_months = abs(number_of_months)
    year = date.year + int(absolute_months/12) * absolute_months/number_of_months
    month = date.month + (absolute_months % 13) * absolute_months/number_of_months
    if month < 1:
        year -= 1
        month += 12
    elif month > 12:
        year += 1
        month -= 12
    return dt.date(int(year), int(month), 1)


def get_fy_months(fiscal_year_str):
    """gets a string eg. FY16 and return a list of datetimes with each month in the received fiscal year"""
    fiscal_year = int(fiscal_year_str[-2:]) + 2000
    list_of_months = []
    for month_number in range(1,13):
        real_year = fiscal_year
        if month_number + 3 <= 12:
            month_number += 3
        else:
            month_number -= 9
            real_year += 1
        list_of_months.append(dt.date(day=1, month=month_number, year=real_year))
    return list_of_months


def get_list_of_weeks(date_to, date_from):
    """gets a list of all weeks number from date_from till date_to"""
    weeks = []
    date_to = get_next_sunday(date_to)
    while date_from <= date_to:
        weeks.append(date_from.isocalendar()[:2])
        date_from = date_from + dt.timedelta(weeks=1)
    return weeks


def get_days_of_month(date):
    """get list of all days of a given month"""
    num_days = calendar.monthrange(date.year, date.month)[1]
    return [dt.date(date.year, date.month, day) for day in range(1, num_days + 1)]


def get_list_of_mondays(date_to, date_from):
    """gets a list of all mondays from date_from till date_to"""
    mondays = []
    date_from = get_previous_monday(date_from)
    while date_from <= date_to:
        mondays.append(date_from)
        date_from = date_from + dt.timedelta(weeks=1)
    return mondays


def get_list_of_quarters(from_date, to_date):
    """get list of quarters (tuple(int:year, int:quarter[1-4]))"""
    start_year, start_quarter = get_quarter_fy(from_date)
    end_year, end_quarter = get_quarter_fy(to_date)
    pivot_quarter = start_quarter
    pivot_year = start_year
    list_of_quarters = []
    while pivot_year <= end_year:
        while pivot_quarter <= 4 and (pivot_year < end_year or pivot_quarter <= end_quarter):
            list_of_quarters.append((pivot_year, pivot_quarter))
            pivot_quarter += 1
        pivot_quarter = 1
        pivot_year += 1
    return list_of_quarters


def get_next_sunday(date):
    return date + dt.timedelta(days=(6 - date.weekday()))

# if date is monday, it returns date
def get_previous_monday(date):
    return date - dt.timedelta(days=(date.weekday()))


def get_list_of_days(to_date, from_date, max_days=None):
    delta = to_date - from_date
    number_of_days_to_fecth = min(delta.days + 1, max_days or delta.days + 1)
    return [to_date - dt.timedelta(days=day-1) for day in range(number_of_days_to_fecth, 0, -1)]


def get_list_of_months(to_date, from_date):
    months=[]
    while from_date <= to_date:
        months.append(from_date.replace(day=1))
        from_date = get_last_day_of_month(from_date) + dt.timedelta(days=1)

    return months


def get_days_of_week(year=None, week=None, day=None):
    if day is not None and year is None and week is None:
        week = day.isocalendar()[1]
        year = day.year
    from_day, _ = get_week_borders(year,week)
    return [ from_day + dt.timedelta(days=i) for i in range(7) ]


def get_week_borders(year, week):
    #The ISO 8601 definition for week 01 is the week with the year's first Thursday in it. Python calendar does it differently
    if dt.date(year,1,1).weekday() < 4:
        week = week - 1
    end = dt.datetime.strptime("{}-W{}-0".format(year,week), "%Y-W%W-%w")
    start = dt.datetime.strptime("{}-W{}-1".format(year,week), "%Y-W%W-%w")
    return start.date(),end.date()


def get_quarter_fy(date):
    year = date.year - (1 if date.month < 4 else 0)
    quarter = (12 if date.month < 4 else date.month - 1) // 3
    return year,quarter


def get_fy_limits(date):
    if type(date) == str:
        year = int(date[-2:]) + 2000
    elif type(date) == dt.date:
        year = date.year - (1 if date.month<4 else 0)
    else:
        raise Exception("Couldn't convert fiscal year {0}".format(date))
    start_date = dt.date(year, 4, 1)
    end_date = dt.date(year + 1, 3, 31)
    return start_date, end_date

def months_between(d1,d2):
    dtemp = d1
    while dtemp <= d2:
        yield dtemp
        if dtemp.month < 12:
            dtemp = dtemp.replace(month=dtemp.month+1)
        else:
            dtemp = dtemp.replace(month=1, year=dtemp.year+1)

def days_between(d1,d2):
    dtemp = d1
    while dtemp <= d2:
        yield dtemp
        dtemp += dt.timedelta(days=1)


def get_last_day_of_month(date):
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def get_months_from_quarter(fiscal_year,quarter):
    return get_fy_months(fiscal_year)[(quarter-1)*3:(quarter-1)*3+3]