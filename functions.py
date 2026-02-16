import datetime

def get_days_from_today(target_date: str) -> int | None:
    if not isinstance(target_date, str):
        return None
    
    format_date = '%Y-%m-%d'

    try:
        target_date = datetime.date.strptime(target_date, format_date)
    except ValueError:
        return None
    
    current_date = datetime.date.today()
    return (current_date - target_date).days
