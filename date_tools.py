import datetime as dt
import calendar


def get_days_of_week_within_month(year, month, week):
    if month == 1 and week > 5:
        year -= 1
    days_of_week = get_days_of_week(year, week)
    return [day for day in days_of_week if day.month == month]


def get_days_of_week(year, week):
    from_day, _ = get_week_borders(year, week)
    return [from_day + dt.timedelta(days=i) for i in range(7)]


def get_week_borders(year, week):
    # The ISO 8601 definition for week 01 is the week with the year's first Thursday in it. Python calendar does it differently
    if dt.date(year, 1, 1).weekday() < 4:
        week = week - 1
    end = dt.datetime.strptime("{}-W{}-0".format(year, week), "%Y-W%W-%w")
    start = dt.datetime.strptime("{}-W{}-1".format(year, week), "%Y-W%W-%w")
    return start.date(), end.date()

def get_list_of_days(to_date, from_date, max_days):
    delta = to_date - from_date
    number_of_days_to_fecth = min(delta.days + 1, max_days)
    return [to_date - dt.timedelta(days=day-1) for day in range(number_of_days_to_fecth, 0, -1)]

def get_list_of_months(to_date, from_date):
    months=[]
    while from_date <= to_date:
        months.append(from_date.replace(day=1))
        from_date = (from_date + dt.timedelta(days=32)).replace(day=1)

    return months

def get_fy_months(fiscal_year):
    list_of_months = []
    for i in list(range(4,13)) + list(range(1,4)):
        list_of_months.append(calendar.month_name[i] + " " + fiscal_year[-2:])
    return list_of_months