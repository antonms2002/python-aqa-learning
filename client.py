import allure
import requests
import logging

logger = logging.getLogger(__name__)

class BookerClient:
    def __init__(self, base_url='https://restful-booker.herokuapp.com'):
        # 1. Задаем базовый URL и заголовки по умолчанию
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        self.token = None  # Пока токена нет
        self._endpoint = 'booking'

    @allure.step("Авторизация")
    def authorize(self, username, password):
        auth_body = {"username": username,
                     "password": password}
        response_auth = requests.post(url=f"{self.base_url}/auth", json=auth_body, headers=self.headers)
        response_json = response_auth.json()
        if response_auth.status_code == 200 and "token" in response_json:
            logger.info("Авторизация прошла успешно")
        else:
            raise Exception(f"❌ Авторизация НЕ успешна: {response_auth.text}")
        self.token = response_json["token"]
        self.headers["Cookie"] = f"token={self.token}"

    @allure.step("Создание букинга")
    def create_booking(self, payload):
        logger.info("Создание нового букинга")
        response_create_booking = requests.post(url=f"{self.base_url}/{self._endpoint}", json=payload,headers=self.headers)
        return response_create_booking

    @allure.step("Удаление букинга")
    def delete_booking(self, booking_id):
        logger.info(f"Удаление букинга id={booking_id}")
        response_delete_booking = requests.delete(url=f"{self.base_url}/{self._endpoint}/{booking_id}", headers=self.headers)
        return response_delete_booking

    @allure.step("Получение букинга")
    def get_booking(self, booking_id):
        logger.info(f"Получение букинга id={booking_id}")
        response_get_booking = requests.get(url=f"{self.base_url}/{self._endpoint}/{booking_id}", headers=self.headers)
        return response_get_booking

    @allure.step("Обновление букинга")
    def update_booking(self, booking_id, payload):
        logger.info(f"Обновление букинга id={booking_id}")
        response_update_booking = requests.put(url=f"{self.base_url}/{self._endpoint}/{booking_id}", json=payload, headers=self.headers)
        return response_update_booking