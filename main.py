import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel():
    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket():
    def generate(self):
        pass


hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket()
    print(reservation_ticket.generate())

else :
    print('Hotel is not free.')
