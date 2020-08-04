from abc import ABC, abstractmethod
class jewelry(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind
#of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass
class CreditCardPayment(jewelry):
#here we've defined how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = CreditCardPayment()
obj.paySlip("$300")
obj.payment("$300")
