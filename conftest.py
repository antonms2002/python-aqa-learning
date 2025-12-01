import requests
import pytest
from client import BookerClient

@pytest.fixture(scope="session")
def booker():
    # 1. Создаем объект
    api = BookerClient()

    # 2. Сразу авторизуем его (один раз на всю сессию!)
    api.authorize("admin", "password123")

    # 3. Отдаем готового, заряженного робота в тесты
    yield api

    print("done")

@pytest.fixture
def create_booking_body():
    create_booking_body = {
        "firstname": "Jim",
        "lastname": "Anton",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return create_booking_body