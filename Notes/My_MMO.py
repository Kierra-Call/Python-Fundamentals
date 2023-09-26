class Stuff:
    def __init__(self, stuff):
        self.stuff = stuff

class Ability:
    #constructor
    def __init__(self):
        pass
class Character:

    #constructor
    #self is the instance
    def __init__(self, name, health, race, mana, stamina): # Init creates a space in memory
        self.name = name
        self.health = health
        self.race = race
        self.mana = mana
        self.stamina = stamina 
        self.stuff = []

    # def __repr__(self) -> str:
    #     return self.name
    

    def info(self):
        print("***************************")
        print(f"Health: {self.health}")
        print(f"Race: {self.race}")
        print(f"Mana: {self.mana}")
        print(f"Stamina: {self.stamina}")
        print(f"Stuff: {self.stuff}")
        return self

    def get_stuff(self, thing):
        self.stuff.append(thing)
        return self

emergency_shwarma = Stuff("Emergency Shwarma")
phone = Stuff("Phone")
c1 = Character("Tyler", 100, "elf", 50, 50)
c2 = Character("Josh", 100, "elf", 50, 50)

print(c1)
print(c2)
c1.get_stuff(emergency_shwarma)
c1.get_stuff(phone)
c1.info()
c2.info()

