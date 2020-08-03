# Python program to  
# demonstrate private members 
  
# Creating a Finance class 
class Finance: 
    def __init__(self): 
        self.a = "Message for all Finance Team members"
        self.__c = "Message for Sales Team within Finance"
  
# Creating a Sales class 
class Sales(Finance): 
    def __init__(self): 
          
        # Calling constructor of 
        # Finance class 
        Finance.__init__(self)  
        print("Calling private member of Finance class: ") 
        print(self.__a) 
# Driver code 
obj1 = Finance() 
print(obj1.a) 
  


