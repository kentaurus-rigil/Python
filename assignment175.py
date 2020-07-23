class Client:
    name = 'No Name Provided'
    email = ''
    password = 'GOGOGO'
    account_number = 0
class Associate(Client):
    base_pay = 11.00
    department = 'General'

class Customer(Client):
    mailing_address = ' '
    mailing_list = True
