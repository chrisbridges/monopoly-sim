class Player:
    def __init__(self, name, token):
        self.name = name
        self.money = 1500
        self.properties_owned = []
        self.get_out_of_jail_cards = 0
        self.token = token
        self.current_position = 0  # Starting at "Go"

    def move(self, steps, board):
        for _ in range(steps):
            self.current_position = board.traverse_board(1)
        return self.current_position

    def buy_property(self, property_name):
        # In a real game, we'd also deduct the purchase price from the player's money
        self.properties_owned.append(property_name)

    def pay_money(self, amount):
        self.money -= amount

    def receive_money(self, amount):
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
