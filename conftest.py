import os
from dotenv import load_dotenv
import pytest
from client import BookerClient
import json

load_dotenv()
current_dir = os.path.dirname(__file__)

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
    create_booking_path = os.path.join(current_dir, "data", "create_booking.json")

    with open(create_booking_path, 'r', encoding='utf-8') as f:
        create_booking_payload = json.load(f)

    return create_booking_payload

@pytest.fixture
def update_booking_body():
    update_booking_path = os.path.join(current_dir, "data", "update_booking.json")

    with open(update_booking_path, 'r', encoding='utf-8') as f:
        update_booking_payload = json.load(f)

    return update_booking_payload