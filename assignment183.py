# Parent Class Participant
class Participant:
    name = "Susan"
    email = "susanp@gmail.com"
    password = "trackstar"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your emails: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


#Child Class Athlete
class Athlete(Participant):
    base_fee = 50.00
    event = "Hurdles"
    pin_number = "2256"


#This is the same method in the parent class "User"
#The difference is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your emails: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#The following code invokes the methods inside each class for Participant and Athlete.

client = Participant()
client.getLoginInfo()

user = Athlete()
user.getLoginInfo()
    
