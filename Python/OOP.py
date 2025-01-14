class a :
    pass

aa = a() # object creation of class a 
bb = a()
print(type(aa))

dir(a)

class car:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"{self.name} is an SUV car")
    
audi = car('audi',5)
print(audi.name)
audi.display()


# class Bank:
#     def __init__(self,owner,balance=0):
        
