import pandas as pd

def load_data(filename):
    """Функція для завантаження даних з файлу CSV"""
    try:
        data = pd.read_csv(filename)
        print("Дані успішно завантажено.")
        return data
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
