import datetime

def get_days_from_today(target_date):
    format_date = '%Y-%m-%d'
    target_date = datetime.date.strptime(target_date, format_date)
    current_date = datetime.date.today()
    return (current_date - target_date).days
