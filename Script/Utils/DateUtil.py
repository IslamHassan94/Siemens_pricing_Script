from datetime import datetime, timedelta


# ReusableAsset_COE00079
def getTodaysDate():
    from datetime import datetime
    today = datetime.today()
    day = today.strftime("%d/%m/%y")
    return str(day)


def getTodaysDate_notifi():
    from datetime import datetime
    today = datetime.today()
    day = today.strftime("%m/%d/%y")
    return str(day)


def getTodaysDate_forSgi():
    from datetime import datetime
    today = datetime.today()
    day = today.strftime("%m/%d/%y")
    return str(day)


def getTodaysDateInSerialFormat():
    from datetime import datetime
    today = datetime.today()
    day = today.strftime('%Y%m%d')
    return str(day)


def get_yesterday_date():
    today = datetime.now()
    if today.weekday() == 0:  # Monday
        # If today is Monday, subtract 3 days to get Friday
        yesterday = today - timedelta(days=3)
    else:
        # Otherwise, subtract 1 day for normal yesterday
        yesterday = today - timedelta(days=1)

    return yesterday.strftime('%d/%m/%Y')


def get_date_diff(forcasted_date, today_date):
    return (forcasted_date - today_date).days
