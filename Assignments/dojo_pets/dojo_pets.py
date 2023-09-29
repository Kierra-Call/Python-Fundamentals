# Ask Tyler about .super().method() vs .self.method()

class Pet:
# implement __init__( name , type , tricks ):

    def __init__(self, name, type, tricks, health = 100, energy = 100):
        
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"Your pet's energy has increased by 25")
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"Your pet's energy has increased by 5 and health by 10")

        return self

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"Your pet's health has increased by 5")
        return self

# noise() - prints out the pet's sound
    def noise(self):
        print("Woof Woof")
        return self

class Ninja (Pet):
# implement __init__( first_name , last_name , treats , pet_food , pet )
    ninjas = []
    def __init__(self, first_name, last_name, pet, treats, pet_food, name, type, tricks, health = 100, energy = 100):
        super().__init__(name, type, tricks, health, energy)
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.ninja_pet = Pet(name, type, tricks, health = 100, energy = 100)
        Ninja.ninjas.append(self)

    @classmethod
    def print_all_ninjas(cls):
        for individual_user in cls.ninjas:
            individual_user.display_ninja()

# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        super().play() #self.pet.play()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        super().eat()
        print(f"Feeding {self.name} {self.pet_food}...")
        return self

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        super().noise()
        return self

    def display_ninja(self):
        user = self.__dict__
        for key in user:
            print(f"{key}: {user[key]}")
        return self

ninja1 = Ninja("Kylie","Underhill", "Cat", "Burger", "10", "Mr. Muffins","Fire","Roll Over", )
ninja2 = Ninja("Phanton","Gerber","Cat","Chicken Biscuit","15","Lane","Shadow","Plotting Scheme")

ninja1.feed().display_ninja() #Feeding the pet
print("******************")
ninja1.bathe().display_ninja()
print("******************")
ninja1.walk().display_ninja()
print("******************")

ninja1.play().display_ninja()
print("******************")
ninja1.eat().display_ninja()
print("******************")
ninja1.play().display_ninja()
print("******************")
ninja1.noise().display_ninja()
print("******************")



# Ninja.print_all_ninjas()





