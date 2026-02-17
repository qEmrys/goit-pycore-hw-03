import datetime
import random
import re

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

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000:
        return list()
    
    if not min < quantity < max:
        return list()
    
    numbers = random.sample(range(min, max), quantity)
    
    return sorted(numbers)

def normalize_phone(phone_number: str) -> str:
    parsed_number = ''.join([char for char in phone_number if char.isdigit()])
    pattern = '38'
    match = re.search(pattern, parsed_number)

    if match:
        return '+' + parsed_number
    
    return '+38' + parsed_number

def get_upcoming_birthdays(users: list) -> list:
    format_date = '%Y.%m.%d'
    congratulation_users = list()

    for user in users:
        current_date = datetime.date.today()
        target_date = datetime.datetime.strptime(user['birthday'], format_date).date()
        target_date_norm = target_date.replace(year=current_date.year)

        if target_date_norm < current_date:
            target_date_norm = target_date_norm.replace(year=current_date.year + 1)

        days_to_birthday = (target_date_norm - current_date).days

        if days_to_birthday <= 7:
            congratulation_date = target_date_norm

            if congratulation_date.weekday() >= 5:
                days_to_add = 7 - congratulation_date.weekday()
                congratulation_date = congratulation_date + datetime.timedelta(days=days_to_add)

            congratulation_users.append(dict())
            congratulation_users[-1]['name'] = user['name']
            congratulation_users[-1]['congratulation_date'] = congratulation_date.strftime('%Y.%m.%d')
        
    return congratulation_users