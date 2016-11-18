import datetime as dt
import calendar


def get_days_of_week_within_month(year, month, week):
    if month == 1 and week > 5:
        year -= 1
    days_of_week = get_days_of_week(year, week)
    return [day for day in days_of_week if day.month == month]

def delta_months(date, number_of_months):
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

def get_fy_months(fiscal_year):
    year = int(fiscal_year[-2:])
    list_of_months = []
    for i in range(4,13):
        list_of_months.append("{} {}".format(calendar.month_name[i], year))
    for i in range(1,4):
        list_of_months.append("{} {}".format(calendar.month_name[i], year + 1))
    return list_of_months

# move to_date to last sunday
def get_list_of_weeks(date_to, date_from):
    weeks = []
    while date_from <= date_to:
        date_from = date_from + dt.timedelta(weeks=1)
        week = date_from.isocalendar()[1]
        weeks.append((date_from.year,week))
    return weeks

def get_days_of_month(date):
    num_days = calendar.monthrange(date.year, date.month)[1]
    return [dt.date(date.year, date.month, day) for day in range(1, num_days + 1)]

def get_list_of_mondays(date_to, date_from):
    mondays = []
    date_from = get_previous_monday(date_from)
    while date_from <= date_to:
        mondays.append(date_from)
        date_from = date_from + dt.timedelta(weeks=1)
    return mondays

def get_list_of_quarters(from_date, to_date):
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

def get_previous_monday(date):
    return date - dt.timedelta(days=(date.weekday()))

def get_list_of_days(to_date, from_date, max_days):
    delta = to_date - from_date
    number_of_days_to_fecth = min(delta.days + 1, max_days)
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

#todo: this is wrong. to be removed
def get_days_of_week_from_date(from_day):
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
    month = (12 if date.month < 4 else date.month - 1) // 3
    return year,month

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

def get_last_day_of_month(date):
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)