import random
from datetime import timedelta, datetime

def random_phone():
    return f"+7{random.randint(1000000000, 9999999999)}"

def random_future_date(days_range=(5, 28)):
    today = datetime.now()
    future_days = random.randint(*days_range)
    future_date = today + timedelta(days=future_days)
    return future_date.strftime("%d.%m.%Y")

# Наборы данных для тестирования
TEST_DATA = [
    (
        "Иван",
        "Иванов",
        "ул. Пушкина, д. 10",
        random_phone(),
        "Буду в красной куртке",
        random_future_date()
    ),
    (
        "Михаил",
        "Сидоров",
        "пер. Цветочный, д. 15",
        random_phone(),
        "Позвонить заранее",
        random_future_date()
    )
]