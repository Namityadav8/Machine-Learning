# #single inheritane 
# class baap:
#     def __init__(self,name,age,childs):
#         self.name = name
#         self.age = age
#         self.childs = childs
    
#     def parent(self):
#         print(f"hello this is {self.name}")
#         print(f"{self.name} has age {self.age}")
        


# class child(baap):
#     def __init__(self,name, age, childs,brothers):
#         super().__init__(name , age,childs)
#         self.brothers = brothers
    
#     def bhai(self):
#         print(f"{self.name} has  brothers")

# bache = child("namit",20,2,0)
# pita = baap("raj",50,2)

# bache.bhai()
# bache.parent()  # calling the function of parent class


#Multiple Inheritance

class dad:
    def __init__(self,name):
        self.name = name

    def nam(self):
        print(f"hello this is {self.name}")
    
class mom:
    def __init__(self,age):
        self.age = age

    def umar(self):
        print(f"{self.age} is the age of mom")

class house(dad,mom):
    def __init__(self, name,age):
        dad.__init__(self,name)
        mom.__init__(self,age)

ghar = house('raj',50)

ghar.nam()
ghar.umar()