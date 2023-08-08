from board import MonopolyBoard
from utils.roll_dice import *
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

    def pay_money(self, amount: int):
        self.money -= amount

    def receive_money(self, amount: int):
        self.money += amount

    def __repr__(self):
        return f"Player(name={self.name}, token={self.token}, money=${self.money}, properties={self.properties_owned})"

# Create two sample players for demonstration
player1 = Player(name="Alice", token="Car")
player2 = Player(name="Bob", token="Hat")

# Move player1 5 spaces
player1.move(5, board)

# Display the players' details
player1, player2
