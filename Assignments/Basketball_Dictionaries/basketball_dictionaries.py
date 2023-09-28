players = [
{
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
},
{
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},
{
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
},
{
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
},
{
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
},
{
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
}
]

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???


class Player:
    all_players = []
    def __init__(self, players):
        self.name = players["name"]
        self.age = players["age"]
        self.position = players["position"]
        self.team = players["team"]
        Player.all_players.append(self)

    # def __init__(self, player):
    # for k,v in player.items():
    #     setattr(self, k, v)
    # Player.all_players.append(self)

    def display_player(self):
        player_attributes = self.__dict__
        for key in player_attributes:
            print(f"{key}: {player_attributes[key]}")
        return self

    @classmethod
    def print_all(cls):
        for individual_player in cls.all_players:
            individual_player.display_player()

    @classmethod
    def teams(cls,list):
        lists = []
        for dictionary in list:
            list.append(cls(dictionary))
        return lists

my_team = Player.teams(players)
for player in all_players:
    print(player.name)

player1 = Player(players[0]).display_player()
print("***********")
player2 = Player(kevin).display_player()
player3 = Player(jason).display_player()
player4 = Player(kyrie).display_player()
print("***********")
Player.print_all()
