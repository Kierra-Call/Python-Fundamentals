class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False #Default set, not taking in information but establishing it
        self.gold_card_points = 0 #Default set, not taking in information but establishing it

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return self #Need to return self in order to chain functions. 
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return self #Need to return self in order to chain functions. 

    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print("Not enough points! :(")
            return self
        else:
            self.gold_card_points -= amount
            return self #Need to return self in order to chain functions. 

user1 = User("Henry", "Hen", "henry@gmail.com", 19)

user1.enroll().display_info() #Displaying information about the user
# user1..display_info() #Enrolling user1 and adding credits to account and displaying the data

user2 = User("Brittany", "Lovelace", "BLovelace@gmail.com", 25)
user3 = User("Tommy", "Yoland", "tommy@gmail.com", 29)

user1.spend_points(50).display_info() #Spending 50 points in this user's instance and displaying the data
user2.enroll().spend_points(80).display_info() #Enrolling second user and displaying the data
# user2.display_info() #Having second user spend 80 points and displaying the data

user1.display_info() #Displaying info
user2.display_info() #Displaying info
user3.display_info() #Displaying info

user1.enroll() #Attempting to reenroll the first user --  instead gets "User is already a member" -- as expected

user2.spend_points(201).display_info() #Attempting to spend more points than the user currently has.
