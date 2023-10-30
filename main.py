import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel():
    def __init__(self, hid):
        self.hid = hid


    def book(self):
        ''' Books a hotel by changing available option'''
        df.loc[df['id'] == self.hid, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        ''' Checks if the hotel is available '''
        availability = df.loc[df['id'] == self.hid, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket():
    def generate(self):
        pass


print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket()
    print(reservation_ticket.generate())

else :
    print('Hotel is not free.')
