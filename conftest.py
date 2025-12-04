import os
from dotenv import load_dotenv
import pytest
from client import BookerClient

load_dotenv()

@pytest.fixture(scope="session")
def booker():
    # 1. Создаем объект
    api = BookerClient()

    username = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    # 2. Сразу авторизуем его (один раз на всю сессию!)
    api.authorize(username, password)

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

@pytest.fixture
def update_booking_body():
    update_booking_body = {
    "firstname" : "Donald",
    "lastname" : "Trump",
    "totalprice" : 777,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-03"
    }
    }
    return update_booking_body