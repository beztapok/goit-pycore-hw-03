import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує випадковий набір унікальних чисел у заданому діапазоні.

    Параметри:
    min (int): мінімальне можливе число у наборі (не менше 1).
    max (int): максимальне можливе число у наборі (не більше 1000).
    quantity (int): кількість чисел, які потрібно вибрати (не може бути більше ніж max - min + 1).

    Повертає:
    list: Відсортований список випадково вибраних, унікальних чисел.
          Пустий список, якщо параметри не відповідають обмеженням.
    """
    # Перевірка вхідних параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    # Використання random.sample для генерації унікальних чисел у заданому діапазоні
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Відсортування чисел перед поверненням
    return sorted(numbers)

# Приклад використання функції
if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
