import pytest
from schemas import CreateBooking

def test_create_and_delete_booking(booker, create_booking_body):

    response_create_booking = booker.create_booking(payload=create_booking_body)

    # Создаем экзмеляр класса, который описывает response create booking
    object_create_booking = CreateBooking(**response_create_booking.json())

    booking_id = object_create_booking.bookingid
    assert object_create_booking.booking.lastname == "Anton", "Last Name should be Anton"
    assert response_create_booking.status_code == 200, "Create Booking Status Code should be 200"

    response_delete_booking = booker.delete_booking(booking_id=booking_id)
    assert response_delete_booking.status_code == 201, "Delete Booking Status Code should be 200"

    response_get_booking = booker.get_booking(booking_id=booking_id)
    assert response_get_booking.status_code == 404, "Get Booking Status Code should be 404"

