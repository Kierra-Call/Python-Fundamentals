#classes use Pascel case: starts with uppercase and every other word uppercase: RoomLamp.
class Lamp:
    # Constructor function || Magic Method
    def __init__(self, name): #Creating a lamp
        #Attributes
        self.name = name

    #methods
    def change_name(self, new_name):
        self.name = new_name
        #Returns nothing!
    def info(self):
        print(self.name)
        return self

lamp1 = Lamp("Percy") #Store the instance
lamp2 = Lamp("Pixar")
print(lamp1.name) #Percy
print(lamp2.name) #Pixar
lamp1.info().change_name("Tyler") #Becomes None because it returns nothing
lamp2.info()

lamp1.change_name("Shwarma")
print("*"*80) #*************
print(lamp1.name) #Shwarma
print(lamp2.name) #Pixar