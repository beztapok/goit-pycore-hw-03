import datetime

def set_fixed_date(current_date):
    # Ставимо фіксовану дату для тестування
    datetime.datetime.today = lambda: current_date

# Фіксуємо дату "2024.01.22" для тестування
fixed_date = datetime.datetime.strptime("2024.01.22", "%Y.%m.%d")
set_fixed_date(fixed_date)

# Тепер викликаємо функцію get_upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
