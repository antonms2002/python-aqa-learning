from pydantic import BaseModel

#Схема create booking и update booking
class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: float
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None

class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking







