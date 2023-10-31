import pandas as pd

# Reading all the csv files into dataframes
df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_secure = pd.read_csv('card_security.csv', dtype=str)


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


class Spa(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        ''' Generates a bookings reservation '''
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

    def validate(self, expiration, cvc, holder):
        ''' Validates the credit card details with the df_cards'''
        card_dict = {'number': self.number, 'expiration': expiration, 'cvc': cvc, 'holder': holder}
        if card_dict in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, password):
        ''' Authenticates the creditcard with its password. '''
        pass_w = df_cards_secure.loc[df_cards_secure['number'] == self.number, ['password']].squeeze()
        if pass_w == password:
            return True


class SpaReservation():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        ''' Generates the SPA Reservation '''
        content = f'''

        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel_object.hotel_name}

        '''
        return content

# List all the hotels
print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
# Checks hotel availability
if hotel.available():
    creditcard = SecureCreditCard(number='1234')
    # Validates the Credit Card
    if creditcard.validate(expiration='12/26', cvc='123', holder='JOHN SMITH'):
        # Authenticates the card with its password
        if creditcard.authenticate(password='mypass'):
            print('Credit card authenticated.')
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa_choice = input('Do you want to book a spa package?')
            # Prints Spa reservation when notified.
            if spa_choice == 'yes':
                spa_reservation = SpaReservation(customer_name=name, hotel_object=hotel)
                print(spa_reservation.generate())
        else:
            print('Credit Card not Authenticated.')
    else:
        print('Creditcard payment failed.')

else:
    print('Hotel is not free.')
