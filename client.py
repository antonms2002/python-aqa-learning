import requests


class BookerClient:
    def __init__(self):
        # 1. Задаем базовый URL и заголовки по умолчанию
        self.base_url = "https://restful-booker.herokuapp.com"
        self.headers = {"Content-Type": "application/json"}
        self.token = None  # Пока токена нет

    def authorize(self, username, password):
        auth_body = {"username": username,
                     "password": password}
        response_auth = requests.post(url=f"{self.base_url}/auth", json=auth_body, headers=self.headers)
        self.token = response_auth.json()["token"]
        self.headers["Cookie"] = f"token={self.token}"
        pass

    def create_booking(self, payload):
        response_create_booking = requests.post(url=f"{self.base_url}/booking", json=payload,headers=self.headers)
        return response_create_booking

    def delete_booking(self, booking_id):
        response_delete_booking = requests.delete(url=f"{self.base_url}/booking/{booking_id}", headers=self.headers)
        return response_delete_booking

    def get_booking(self, booking_id):
        response_get_booking = requests.get(url=f"{self.base_url}/booking/{booking_id}", headers=self.headers)
        return response_get_booking