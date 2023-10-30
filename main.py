import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')


class Hotel():
    def __init__(self, hid):
        self.hid = hid
        self.hotel_name = df.loc[df['id'] == self.hid, 'name'].squeeze()

    def book(self):
        '''
        Books a hotel by setting availability option to no
        '''
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
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f'''
        
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}
        
        '''
        return content


class CreditCard():
    def __init__(self, number):
        self.number = number

    def validate(self,expiration, cvc, holder):
        card_dict = {'number': self.number, 'expiration': expiration,
                         'cvc': cvc, 'holder': holder}
        if card_dict in df_cards:
            return True
        else:
            return False


print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
if hotel.available():
    creditcard = CreditCard(number='1234')
    if creditcard.validate(expiration='12/26', cvc='123', holder='JOHN SMITH'):
        print('Credit Card details verified')
        hotel.book()
        name = input('Enter your name: ')
        reservation_ticket = ReservationTicket(customer_name= name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print('Creditcard  payment failed.')

else:
    print('Hotel is not free.')
