import requests


class BookerClient:
    def __init__(self, base_url='https://restful-booker.herokuapp.com'):
        # 1. Задаем базовый URL и заголовки по умолчанию
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        self.token = None  # Пока токена нет
        self._endpoint = 'booking'

    def authorize(self, username, password):
        auth_body = {"username": username,
                     "password": password}
        response_auth = requests.post(url=f"{self.base_url}/auth", json=auth_body, headers=self.headers)
        self.token = response_auth.json()["token"]
        self.headers["Cookie"] = f"token={self.token}"


    def create_booking(self, payload):
        response_create_booking = requests.post(url=f"{self.base_url}/{self._endpoint}", json=payload,headers=self.headers)
        return response_create_booking

    def delete_booking(self, booking_id):
        response_delete_booking = requests.delete(url=f"{self.base_url}/{self._endpoint}/{booking_id}", headers=self.headers)
        return response_delete_booking

    def get_booking(self, booking_id):
        response_get_booking = requests.get(url=f"{self.base_url}/{self._endpoint}/{booking_id}", headers=self.headers)
        return response_get_booking

    def update_booking(self, booking_id, payload):
        response_update_booking = requests.put(url=f"{self.base_url}/{self._endpoint}/{booking_id}", json=payload, headers=self.headers)
        return response_update_booking