import datetime
import random

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

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return list()
    
    if not min < quantity < max:
        return list()
    
    numbers = random.sample(range(min, max), quantity)
    
    return sorted(numbers)