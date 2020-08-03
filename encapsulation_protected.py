# Python program to 
# demonstrate protected members 
  
  
# Creating a Finance class 
class Finance: 
    def __init__(self): 
          
        # Protected member 
        self._a = 2
  
# Creating a Sales class     
class Sales(Finance): 
    def __init__(self): 
          
        # Calling constructor of 
        # Finance class 
        Finance.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._a) 
  
obj1 = Finance() 
          
obj2 = Sales() 
  
# Calling protected member 
# Outside class will result in  
# AttributeError 
print(obj2.a) 
