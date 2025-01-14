class baap:
    def __init__(self,name,age,childs):
        self.name = name
        self.age = age
        self.childs = childs
    
    def parent(self):
        print(f"hello this is {self.name}")
        print(f"{self.name} has age {self.age}")
        


class child(baap):
    def __init__(self,name, age, childs,brothers):
        super().__init__(name , age,childs)
        self.brothers = brothers
    
    def bhai(self):
        print(f"{self.name} has  brothers")

bache = child("namit",20,2,0)
pita = baap("raj",50,2)

bache.bhai()
bache.parent()  # calling the function of parent class
