import random

class Character:
    all_characters = []
    def __init__(self, name, health=30, power=8, armor=8, speed=8):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.speed = speed
        Character.all_characters.append(self)

    #show Info
    def stats(self):
        character_attributes = self.__dict__
        for key in character_attributes:
            print(f"{key}: {character_attributes[key]}")
        return self

    def gain_health(self, amount):
        print(f"{self.name} is losing {amount} health")
        self.health += amount
        return self

    def lose_health(self, amount):
        print(f"{self.name} is losing {amount} health")
        self.health -= amount
        return self

    def attack(self, target):
        damage_amount = random.randint(0, self.power)
        #crit fail
        if damage_amount == 0:
            fall_damage = (self.power / 2)
            self.lose_health(fall_damage)
        #do the damage
        if not target.defence(self):
            target.lose_health(damage_amount)

        return self

    def defence(self, attacker):
        speed_roll = random.randint(1, 20)
        if speed_roll <= self.speed:
            print(f"{self.name} successfully dodged attack")
            return True
        return False

c1 = Character("Bob")
c2 = Character("Tom")

while c1.health > 0 and c2.health > 0:
    c1.attack(c2)
    c2.stats()
    print("****************")