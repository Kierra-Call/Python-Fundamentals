#Encapsulation
# Think of this like a pill containing variables/attributes and methods and the pill is the class 
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")
#Inheritance
#When we inherent something from the parent class 
class CappuccinoM( CoffeeM ): #Coffee maker is the parent class
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
#Polymorphism - (many-forms)
#While our main CoffeeM has a clean method but now we override it with what we did in our CappuccinoM function clean()
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")
#Abstraction
#Where we can hide attributes and methods used to restrict data. For example, a barista does not need to change temp with CoffeeM. Makes debugging harder without.
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self, beans):
        self.cafe.brew_now(beans)




