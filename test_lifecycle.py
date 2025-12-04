import pytest
from schemas import BookingResponse
from schemas import Booking
import allure

@allure.feature("Booking Operations")
class TestLifecycle:

    # Группа "Операции с бронью"
    @allure.story("Positive")  # Подгруппа "Создание и Удаление"
    @allure.title("Проверка полного цикла: Создание -> Удаление")
    @pytest.mark.smoke
    def test_create_and_delete_booking(self, booker, create_booking_body):
        response_create_booking = booker.create_booking(payload=create_booking_body)

        # Создаем экзмеляр класса, который описывает response create booking
        object_create_booking = BookingResponse(**response_create_booking.json())

        booking_id = object_create_booking.bookingid
        assert object_create_booking.booking.lastname == "Anton", "Last Name should be Anton"
        assert response_create_booking.status_code == 200, "Create Booking Status Code should be 200"

        response_delete_booking = booker.delete_booking(booking_id=booking_id)
        assert response_delete_booking.status_code == 201, "Delete Booking Status Code should be 200"

        response_get_booking = booker.get_booking(booking_id=booking_id)
        assert response_get_booking.status_code == 404, "Get Booking Status Code should be 404"
  # Группа "Операции с бронью"
    @allure.story("Positive")  # Подгруппа "Создание и Удаление"
    @allure.title("Обновление букинга")
    @pytest.mark.smoke
    def test_update_booking(self, booker, update_booking_body, create_booking_body):
        response_create_booking = booker.create_booking(payload=create_booking_body)
        object_create_booking = BookingResponse(**response_create_booking.json())
        booking_id = object_create_booking.bookingid

        object_update_booking_request = Booking(**update_booking_body)
        response_update_booking = booker.update_booking(booking_id=booking_id, payload=update_booking_body)
        object_update_booking = Booking(**response_update_booking.json())

        assert object_update_booking_request.lastname == object_update_booking.lastname, "PUT request body is not equal to response body"

        booker.delete_booking(booking_id=booking_id)

    @allure.story("Negative")  # Подгруппа "Создание и Удаление"
    @allure.title("Невалидный токен")
    @pytest.mark.critical_path
    def test_invalid_token(self, booker, create_booking_body):
        response_create_booking = booker.create_booking(payload=create_booking_body)
        assert response_create_booking.status_code == 200, "Create Booking Status Code should be 200"
        # Создаем экзмеляр класса из схемы, который описывает response create booking
        object_create_booking = BookingResponse(**response_create_booking.json())
        booking_id = object_create_booking.bookingid

        # Сохраняем дефолтные хедеры в переменную
        correct_headers = booker.headers.copy()
        # Портим хедеры в самом класее в client
        booker.headers["Cookie"] = "brrr"

        response_delete_booking = booker.delete_booking(booking_id=booking_id)
        assert response_delete_booking.status_code == 403, "Delete Booking Status Code should be 403"

        # Возвращаем в класс корректные хедеры
        booker.headers = correct_headers.copy()

        assert booker.delete_booking(booking_id=booking_id).status_code == 201, "Delete booking Status is not 201"






