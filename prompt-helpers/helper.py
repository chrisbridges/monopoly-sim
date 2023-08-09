class BoardSpace:
    def __init__(self, name, space_type, details=None):
        self.name = name
        self.space_type = space_type
        self.details = details if details else {}
        self.next_space = None

class MonopolyBoard:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_space(self, name, space_type, details=None):
        new_space = BoardSpace(name, space_type, details)
        if not self.head:
            self.head = new_space
            self.tail = new_space
            self.tail.next_space = self.head  # Making it circular
        else:
            self.tail.next_space = new_space
            self.tail = new_space
            self.tail.next_space = self.head  # Making it circular

    def traverse_board(self, steps):
        # FIXME: do I need this if player position is tracked there?
        # This function will simulate a player's movement on the board
        # TODO: does this properly traverse moving backwards?
        current = self.head
        for _ in range(steps):
            current = current.next_space
        return current.name

    def get_space(self, name):
        # This function will return a space by its name
        current = self.head
        while True:
            if current.name == name:
                return current
            current = current.next_space
            if current == self.head:
                break
        return None


# Complete Monopoly board spaces with their names, types, and details (if any)
spaces = [
    ("Go", "Go"),
    ("Mediterranean Avenue", "Property", {"purchase_price": 60, "base_rent": 2, "mortgage_value": 30}),
    ("Community Chest", "Community Chest"),
    ("Baltic Avenue", "Property", {"purchase_price": 80, "base_rent": 4, "mortgage_value": 40}),
    ("Income Tax", "Tax", {"tax_amount": 200}),
    ("Reading Railroad", "Railroad", {"purchase_price": 200}),
    ("Oriental Avenue", "Property", {"purchase_price": 100, "base_rent": 6, "mortgage_value": 50}),
    ("Chance", "Chance"),
    ("Vermont Avenue", "Property", {"purchase_price": 100, "base_rent": 6, "mortgage_value": 50}),
    ("Connecticut Avenue", "Property", {"purchase_price": 120, "base_rent": 8, "mortgage_value": 60}),
    ("Jail", "Jail"),
    ("St. Charles Place", "Property", {"purchase_price": 140, "base_rent": 10, "mortgage_value": 70}),
    ("Electric Company", "Utility", {"purchase_price": 150}),
    ("States Avenue", "Property", {"purchase_price": 140, "base_rent": 10, "mortgage_value": 70}),
    ("Virginia Avenue", "Property", {"purchase_price": 160, "base_rent": 12, "mortgage_value": 80}),
    ("Pennsylvania Railroad", "Railroad", {"purchase_price": 200}),
    ("St. James Place", "Property", {"purchase_price": 180, "base_rent": 14, "mortgage_value": 90}),
    ("Community Chest", "Community Chest"),
    ("Tennessee Avenue", "Property", {"purchase_price": 180, "base_rent": 14, "mortgage_value": 90}),
    ("New York Avenue", "Property", {"purchase_price": 200, "base_rent": 16, "mortgage_value": 100}),
    ("Free Parking", "Free Parking"),
    ("Kentucky Avenue", "Property", {"purchase_price": 220, "base_rent": 18, "mortgage_value": 110}),
    ("Chance", "Chance"),
    ("Indiana Avenue", "Property", {"purchase_price": 220, "base_rent": 18, "mortgage_value": 110}),
    ("Illinois Avenue", "Property", {"purchase_price": 240, "base_rent": 20, "mortgage_value": 120}),
    ("B. & O. Railroad", "Railroad", {"purchase_price": 200}),
    ("Atlantic Avenue", "Property", {"purchase_price": 260, "base_rent": 22, "mortgage_value": 130}),
    ("Ventnor Avenue", "Property", {"purchase_price": 260, "base_rent": 22, "mortgage_value": 130}),
    ("Water Works", "Utility", {"purchase_price": 150}),
    ("Marvin Gardens", "Property", {"purchase_price": 280, "base_rent": 24, "mortgage_value": 140}),
    ("Go to Jail", "Go to Jail"),
    ("Pacific Avenue", "Property", {"purchase_price": 300, "base_rent": 26, "mortgage_value": 150}),
    ("North Carolina Avenue", "Property", {"purchase_price": 300, "base_rent": 26, "mortgage_value": 150}),
    ("Community Chest", "Community Chest"),
    ("Pennsylvania Avenue", "Property", {"purchase_price": 320, "base_rent": 28, "mortgage_value": 160}),
    ("Short Line", "Railroad", {"purchase_price": 200}),
    ("Chance", "Chance"),
    ("Park Place", "Property", {"purchase_price": 350, "base_rent": 35, "mortgage_value": 175}),
    ("Luxury Tax", "Tax", {"tax_amount": 100}),
    ("Boardwalk", "Property", {"purchase_price": 400, "base_rent": 50, "mortgage_value": 200})
]

# rent value for each property
rent_values = {
    "Mediterranean Avenue": [10, 30, 90, 160, 250],
    "Baltic Avenue": [20, 60, 180, 320, 450],
    "Oriental Avenue": [30, 90, 270, 400, 550],
    "Vermont Avenue": [30, 90, 270, 400, 550],
    "Connecticut Avenue": [40, 100, 300, 450, 600],
    "St. Charles Place": [50, 150, 450, 625, 750],
    "States Avenue": [50, 150, 450, 625, 750],
    "Virginia Avenue": [60, 180, 500, 700, 900],
    "St. James Place": [70, 200, 550, 750, 950],
    "Tennessee Avenue": [70, 200, 550, 750, 950],
    "New York Avenue": [80, 220, 600, 800, 1000],
    "Kentucky Avenue": [90, 250, 700, 875, 1050],
    "Indiana Avenue": [90, 250, 700, 875, 1050],
    "Illinois Avenue": [100, 300, 750, 925, 1100],
    "Atlantic Avenue": [110, 330, 800, 975, 1150],
    "Ventnor Avenue": [110, 330, 800, 975, 1150],
    "Marvin Gardens": [120, 360, 850, 1025, 1200],
    "Pacific Avenue": [130, 390, 900, 1100, 1275],
    "North Carolina Avenue": [130, 390, 900, 1100, 1275],
    "Pennsylvania Avenue": [150, 450, 1000, 1200, 1400],
    "Park Place": [175, 500, 1100, 1300, 1500],
    "Boardwalk": [200, 600, 1400, 1700, 2000]
}

updated_spaces = []

def add_rent_values_to_spaces():
# Add the rent information to the spaces list
    for space in spaces:
        if space[1] == "Property":
            property_name = space[0]
            if property_name in rent_values:
                rent_info = rent_values[property_name]
                rents = {
                    1: rent_info[0],
                    2: rent_info[1],
                    3: rent_info[2],
                    4: rent_info[3],
                    5: rent_info[4]  # 5 houses is equivalent to a hotel
                }
                updated_space = (space[0], space[1], {**space[2], "rents": rents})
                updated_spaces.append(updated_space)
            else:
                updated_spaces.append(space)
        else:
            updated_spaces.append(space)

    return updated_spaces

def add_is_mortgaged_flag():
    # Add "is_mortgaged" key to properties, railroads, and utilities
    for space in updated_spaces:
        if space[1] in ["Property", "Railroad", "Utility"]:
            space[2]["is_mortgaged"] = False

import random

def roll_two_dice():
  """Simulates rolling two dice and returns the results."""
  first_die = random.randint(1, 6)
  second_die = random.randint(1, 6)
  return first_die, second_die

class Player:
    def __init__(self, name: str, token: str):
        self.name = name
        self.money = 1500
        self.properties_owned = []
        self.get_out_of_jail_cards = 0
        self.token = token
        self.current_position = 0  # Starting at "Go"

    def move(self, spaces):
        dice1, dice2 = roll_two_dice()
        if self.is_in_jail:
            if dice1 == dice2:
                print(f'{self.token} rolled doubles {dice1} and {dice2} and leaves the jail.')
                self.is_in_jail = False
                self.num_failed_attempts_to_leave_jail = 0
            else:
                self.num_failed_attempts_to_leave_jail += 1
                if self.num_failed_attempts_to_leave_jail == 3:
                    print(f'{self.token} failed to roll doubles for 3 turns in jail and pays the fine.')
                    self.money -= 50  # Pay the fine
                    self.is_in_jail = False
                    self.num_failed_attempts_to_leave_jail = 0
                else:
                    print(f'{self.token} remains in jail as they did not roll doubles.')
            self.num_consecutive_doubles = 0
        else:
            if dice1 == dice2:
                self.num_consecutive_doubles += 1
            else:
                self.num_consecutive_doubles = 0
            if self.num_consecutive_doubles == 3:
                print(f'{self.token} rolled doubles three times in a row and goes to jail.')
                self.is_in_jail = True
                self.position = spaces.index(('Jail', 'Jail'))  # Send the player to jail
                self.num_consecutive_doubles = 0
            else:
                self.position = (self.position + dice1 + dice2) % len(spaces)  # Move the player
        return dice1, dice2

    def take_turn(self, spaces):
        dice1, dice2 = self.move(spaces)
        print(f'{self.token} rolled {dice1} and {dice2} and landed on {spaces[self.position][0]}.')

    def buy_property(self, property_name):
        # In a real game, we'd also deduct the purchase price from the player's money
        self.properties_owned.append(property_name)

    def attempt_to_buy_property(self, spaces):
        current_space = spaces[self.position]
        if current_space[1] == 'Property' and 'owner' not in current_space[2] and self.money >= current_space[2]['purchase_price']:
            # Buy the property
            self.money -= current_space[2]['purchase_price']
            self.properties_owned(current_space[0])
            current_space[2]['owner'] = self.token
            print(f'{self.token} bought {current_space[0]} for {current_space[2]["purchase_price"]}. Remaining money: {self.money}')

    def pay_money(self, amount: int):
        self.money -= amount

    def receive_money(self, amount: int):
        self.money += amount

    def __repr__(self):
        return f"Player(name={self.name}, token={self.token}, money=${self.money}, properties={self.properties_owned})"
    
player1 = Player(name="Alice", token="Car")
player2 = Player(name="Bob", token="Hat")

players = [player1, player2]