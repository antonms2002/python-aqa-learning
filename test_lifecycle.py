import pytest
from schemas import BookingResponse
from schemas import Booking
import allure
import logging

logger = logging.getLogger(__name__)

@allure.feature("Booking Operations")
class TestLifecycle:

    # Группа "Операции с бронью"
    @allure.story("Positive")  # Подгруппа "Создание и Удаление"
    @allure.title("Проверка полного цикла: Создание -> Удаление")
    @pytest.mark.smoke
    def test_create_and_delete_booking(self, booker, create_booking_body):
        create_booking_body_payload = create_booking_body.copy()
        response_create_booking = booker.create_booking(payload=create_booking_body_payload)

        # Создаем экзмеляр класса, который описывает response create booking
        object_create_booking = BookingResponse(**response_create_booking.json())

        booking_id = object_create_booking.bookingid
        logger.info(f"ID созданного букинга: {booking_id}")
        assert object_create_booking.booking.lastname == "Anton", "Last Name should be Anton"
        assert response_create_booking.status_code == 200, "Create Booking Status Code should be 200"

        response_delete_booking = booker.delete_booking(booking_id=booking_id)
        assert response_delete_booking.status_code == 201, "Delete Booking Status Code should be 201"

        response_get_booking = booker.get_booking(booking_id=booking_id)
        assert response_get_booking.status_code == 404, "Get Booking Status Code should be 404"

  # Группа "Операции с бронью"
    @allure.story("Positive")  # Подгруппа "Создание и Удаление"
    @allure.title("Обновление букинга")
    @pytest.mark.smoke
    def test_update_booking(self, booker, update_booking_body, create_booking_body):
        create_booking_body_payload = create_booking_body.copy()
        response_create_booking = booker.create_booking(payload=create_booking_body_payload)
        object_create_booking = BookingResponse(**response_create_booking.json())

        booking_id = object_create_booking.bookingid
        logger.info(f"ID созданного букинга: {booking_id}")

        update_booking_payload = update_booking_body.copy()
        object_update_booking_request = Booking(**update_booking_payload)
        response_update_booking = booker.update_booking(booking_id=booking_id, payload=update_booking_payload)
        object_update_booking = Booking(**response_update_booking.json())

        assert object_update_booking_request.lastname == object_update_booking.lastname, "PUT request body is not equal to response body"

        booker.delete_booking(booking_id=booking_id)

    @allure.story("Negative")  # Подгруппа "Создание и Удаление"
    @allure.title("Невалидный токен")
    @pytest.mark.critical_path
    def test_invalid_token(self, booker, create_booking_body):
        create_booking_body_payload = create_booking_body.copy()
        response_create_booking = booker.create_booking(payload=create_booking_body_payload)
        assert response_create_booking.status_code == 200, "Create Booking Status Code should be 200"
        # Создаем экзмеляр класса из схемы, который описывает response create booking
        object_create_booking = BookingResponse(**response_create_booking.json())
        booking_id = object_create_booking.bookingid
        logger.info(f"ID созданного букинга: {booking_id}")
        # Сохраняем дефолтные хедеры в переменную
        correct_headers = booker.headers.copy()
        # Портим хедеры в самом класее в client
        booker.headers["Cookie"] = "brrr"

        logger.info("Пытаемся удалить букинг, используя невалидный токен")
        response_delete_booking = booker.delete_booking(booking_id=booking_id)
        assert response_delete_booking.status_code == 403, "Invalid token: delete Booking Status Code should be 403"
        logger.info("ОК. Статус-код 403, букинг не удалился")

        # Возвращаем в класс корректные хедеры
        booker.headers = correct_headers.copy()
        logger.info("Удаляем букинг, используя валидный токен")
        assert booker.delete_booking(booking_id=booking_id).status_code == 201, "Delete booking Status is not 201"






