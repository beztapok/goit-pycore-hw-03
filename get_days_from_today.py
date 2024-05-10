import datetime

def get_days_from_today(date_str):
    """
    Розраховує кількість днів між заданою датою та поточною датою.

    Параметри:
    date_str (str): Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.

    Повертає:
    int: Кількість днів від заданої дати до поточної. Якщо задана дата пізніша,
         результат буде від'ємним.

    Помилки:
    ValueError: Якщо формат дати не є 'РРРР-ММ-ДД'.
    """
    try:
        # Перетворення вхідного рядка на об'єкт datetime.date
        input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Отримання поточної дати
        today = datetime.date.today()
        
        # Розрахунок різниці у днях
        difference = input_date - today
        
        # Повернення різниці у днях як ціле число
        return difference.days
    except ValueError:
        # Виняток, якщо формат дати неправильний
        raise ValueError("Please make sure the date is in 'YYYY-MM-DD' format.")

# Приклад використання
print(get_days_from_today("2021-10-09"))  # Приклад поверне -944, якщо сьогодні 24 квітня 2024 року


