from pydantic import BaseModel

class CreateBookingDates(BaseModel):
    checkin: str
    checkout: str

class CreateBookingBooking(BaseModel):
    firstname: str
    lastname: str
    totalprice: float
    depositpaid: bool
    bookingdates: CreateBookingDates
    additionalneeds: str | None = None

class CreateBooking(BaseModel):
    bookingid: int
    booking: CreateBookingBooking

