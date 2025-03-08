import random
import logging
from dataclasses import dataclass, field
from typing import List, Optional

logger = logging.getLogger(__name__)

# --------------------------------------------------------
# 1. Data Structures
# --------------------------------------------------------

@dataclass
class Square:
    name: str
    type: str  # e.g. "property", "railroad", "utility", "tax", "chance", "community_chest", "jail", "go", "free_parking", "go_to_jail"
    position: int
    price: Optional[int] = None
    rent: Optional[List[int]] = None
    color: Optional[str] = None
    owner: Optional[str] = None  # Name or ID of the owning player (None if unowned)

@dataclass
class Player:
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    owned_properties: List[int] = field(default_factory=list)  # store board positions of owned squares

def create_monopoly_board() -> List[Square]:
    """
    Returns a simplified Monopoly board. 
    Rents are from classic Monopoly for demonstration,
    but not all special logic (like railroads/utilities) is implemented here.
    """
    board = [
        Square(name="Go", type="go", position=0),
        Square(name="Mediterranean Avenue", type="property", position=1, price=60, rent=[2, 10, 30, 90, 160, 250], color="brown"),
        Square(name="Community Chest", type="community_chest", position=2),
        Square(name="Baltic Avenue", type="property", position=3, price=60, rent=[4, 20, 60, 180, 320, 450], color="brown"),
        Square(name="Income Tax", type="tax", position=4, price=200),  # We'll treat 'price' here as the tax amount
        Square(name="Reading Railroad", type="railroad", position=5, price=200),
        Square(name="Oriental Avenue", type="property", position=6, price=100, rent=[6, 30, 90, 270, 400, 550], color="light_blue"),
        Square(name="Chance", type="chance", position=7),
        Square(name="Vermont Avenue", type="property", position=8, price=100, rent=[6, 30, 90, 270, 400, 550], color="light_blue"),
        Square(name="Connecticut Avenue", type="property", position=9, price=120, rent=[8, 40, 100, 300, 450, 600], color="light_blue"),
        Square(name="Jail / Just Visiting", type="jail", position=10),
        Square(name="St. Charles Place", type="property", position=11, price=140, rent=[10, 50, 150, 450, 625, 750], color="pink"),
        Square(name="Electric Company", type="utility", position=12, price=150),
        Square(name="States Avenue", type="property", position=13, price=140, rent=[10, 50, 150, 450, 625, 750], color="pink"),
        Square(name="Virginia Avenue", type="property", position=14, price=160, rent=[12, 60, 180, 500, 700, 900], color="pink"),
        Square(name="Pennsylvania Railroad", type="railroad", position=15, price=200),
        Square(name="St. James Place", type="property", position=16, price=180, rent=[14, 70, 200, 550, 750, 950], color="orange"),
        Square(name="Community Chest", type="community_chest", position=17),
        Square(name="Tennessee Avenue", type="property", position=18, price=180, rent=[14, 70, 200, 550, 750, 950], color="orange"),
        Square(name="New York Avenue", type="property", position=19, price=200, rent=[16, 80, 220, 600, 800, 1000], color="orange"),
        Square(name="Free Parking", type="free_parking", position=20),
        Square(name="Kentucky Avenue", type="property", position=21, price=220, rent=[18, 90, 250, 700, 875, 1050], color="red"),
        Square(name="Chance", type="chance", position=22),
        Square(name="Indiana Avenue", type="property", position=23, price=220, rent=[18, 90, 250, 700, 875, 1050], color="red"),
        Square(name="Illinois Avenue", type="property", position=24, price=240, rent=[20, 100, 300, 750, 925, 1100], color="red"),
        Square(name="B. & O. Railroad", type="railroad", position=25, price=200),
        Square(name="Atlantic Avenue", type="property", position=26, price=260, rent=[22, 110, 330, 800, 975, 1150], color="yellow"),
        Square(name="Ventnor Avenue", type="property", position=27, price=260, rent=[22, 110, 330, 800, 975, 1150], color="yellow"),
        Square(name="Water Works", type="utility", position=28, price=150),
        Square(name="Marvin Gardens", type="property", position=29, price=280, rent=[24, 120, 360, 850, 1025, 1200], color="yellow"),
        Square(name="Go To Jail", type="go_to_jail", position=30),
        Square(name="Pacific Avenue", type="property", position=31, price=300, rent=[26, 130, 390, 900, 1100, 1275], color="green"),
        Square(name="North Carolina Avenue", type="property", position=32, price=300, rent=[26, 130, 390, 900, 1100, 1275], color="green"),
        Square(name="Community Chest", type="community_chest", position=33),
        Square(name="Pennsylvania Avenue", type="property", position=34, price=320, rent=[28, 150, 450, 1000, 1200, 1400], color="green"),
        Square(name="Short Line Railroad", type="railroad", position=35, price=200),
        Square(name="Chance", type="chance", position=36),
        Square(name="Park Place", type="property", position=37, price=350, rent=[35, 175, 500, 1100, 1300, 1500], color="dark_blue"),
        Square(name="Luxury Tax", type="tax", position=38, price=100),
        Square(name="Boardwalk", type="property", position=39, price=400, rent=[50, 200, 600, 1400, 1700, 2000], color="dark_blue"),
    ]
    return board

# --------------------------------------------------------
# 2. Game Engine
# --------------------------------------------------------

class MonopolyGame:
    def __init__(self, player_names: List[str]):
        self.board = create_monopoly_board()
        self.players = [Player(name=name) for name in player_names]
        self.current_player_index = 0
        self.game_over = False
        self.turn_count = 0
        # Optional limit to prevent infinite loops in certain edge cases
        self.max_turns = 1000  

    def roll_dice(self) -> int:
        """Simulate a standard 2D6 roll."""
        return random.randint(1, 6) + random.randint(1, 6)

    def next_player(self):
        """Advance to the next player who is still active."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        # Skip bankrupt players (money < 0) in case we haven't removed them
        while self.players[self.current_player_index].money < 0:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def move_player(self, player: Player, steps: int):
        """Move the player around the board and handle passing Go."""
        old_position = player.position
        new_position = (old_position + steps) % len(self.board)
        
        # If we passed 'Go'
        if new_position < old_position:
            player.money += 200
            logger.info(f"{player.name} passed Go! Collect $200. Money: {player.money}")

        player.position = new_position

    def handle_square(self, player: Player):
        """Handle actions based on the square the player lands on."""
        square = self.board[player.position]
        logger.info(f"{player.name} landed on {square.name} ({square.type}).")

        # Check square type
        if square.type == "property":
            self.handle_property(player, square)
        elif square.type == "tax":
            self.handle_tax(player, square)
        elif square.type == "chance":
            self.handle_chance(player)
        elif square.type == "community_chest":
            self.handle_community_chest(player)
        elif square.type == "go_to_jail":
            self.send_to_jail(player)
        # "jail", "go", "free_parking" do nothing special here

    def handle_property(self, player: Player, square: Square):
        """Handle buying or paying rent for a property."""
        if square.owner is None:
            # Decide whether to buy; for simplicity, always buy if we have enough money
            if player.money >= (square.price or 0):
                square.owner = player.name
                player.owned_properties.append(square.position)
                player.money -= square.price
                logger.info(f"{player.name} bought {square.name} for ${square.price}. Remaining money: {player.money}")
        else:
            # Pay rent if owned by someone else
            if square.owner != player.name:
                rent_amount = self.calculate_rent(square)
                player.money -= rent_amount
                # Find owner player object
                for p in self.players:
                    if p.name == square.owner:
                        p.money += rent_amount
                        break
                logger.info(f"{player.name} paid ${rent_amount} in rent to {square.owner}. Remaining money: {player.money}")

    def calculate_rent(self, square: Square) -> int:
        """Very simplified rent calculation."""
        # For demonstration, just use the base rent (index 0) if available
        # or some fallback if rent array is missing.
        if square.rent and len(square.rent) > 0:
            return square.rent[0]
        else:
            # For railroads/utilities, you might define a special logic,
            # but we'll just return a flat 25 for demonstration.
            if square.type in ("railroad", "utility"):
                return 25
            return 10

    def handle_tax(self, player: Player, square: Square):
        """Handle paying income or luxury tax."""
        tax_amount = square.price or 0
        player.money -= tax_amount
        logger.info(f"{player.name} paid a tax of ${tax_amount}. Remaining money: {player.money}")

    def handle_chance(self, player: Player):
        """Simplified Chance card: random effect of either +$50 or -$50."""
        amount = random.choice([50, -50])
        player.money += amount
        if amount > 0:
            logger.info(f"{player.name} drew a Chance card: +${amount}. Money: {player.money}")
        else:
            logger.info(f"{player.name} drew a Chance card: {amount}. Money: {player.money}")

    def handle_community_chest(self, player: Player):
        """Simplified Community Chest: random effect of either +$100 or -$100."""
        amount = random.choice([100, -100])
        player.money += amount
        if amount > 0:
            logger.info(f"{player.name} drew a Community Chest card: +${amount}. Money: {player.money}")
        else:
            logger.info(f"{player.name} drew a Community Chest card: {amount}. Money: {player.money}")

    def send_to_jail(self, player: Player):
        """Send the player to jail."""
        logger.info(f"{player.name} is sent to Jail!")
        player.position = 10  # Jail position
        player.in_jail = True
        player.jail_turns = 0

    def handle_jail(self, player: Player):
        """Handle logic for a player in jail."""
        if player.jail_turns < 2:
            player.jail_turns += 1
            logger.info(f"{player.name} is in jail (turn {player.jail_turns}).")
        else:
            # Release after 3rd turn
            player.in_jail = False
            player.jail_turns = 0
            logger.info(f"{player.name} is released from jail.")

    def check_bankruptcy(self, player: Player):
        """Mark the player as bankrupt if money < 0."""
        if player.money < 0:
            logger.info(f"{player.name} went bankrupt!")
            # Remove ownership of properties
            for pos in player.owned_properties:
                self.board[pos].owner = None
            player.owned_properties.clear()

    def active_players_count(self) -> int:
        """Return how many players are still solvent."""
        return sum(1 for p in self.players if p.money >= 0)

    def play_turn(self):
        """Play a single turn for the current player."""
        player = self.players[self.current_player_index]

        # If player is bankrupt, skip them
        if player.money < 0:
            self.next_player()
            return

        # If player is in jail, handle jail logic
        if player.in_jail:
            self.handle_jail(player)
            # If still in jail, skip move
            if player.in_jail:
                self.next_player()
                return

        # Roll dice and move
        dice_total = self.roll_dice()
        logger.info(f"{player.name} rolls a {dice_total}.")
        self.move_player(player, dice_total)

        # Handle the square effect
        self.handle_square(player)

        # Check if player went bankrupt after landing
        self.check_bankruptcy(player)

        # Next player
        self.next_player()

    def run_game(self):
        """Run the game loop until only one player remains or turn limit is reached."""
        logger.info("Starting Monopoly game!\n")
        while not self.game_over:
            self.turn_count += 1
            self.play_turn()

            # Check if we have a winner
            if self.active_players_count() <= 1:
                self.game_over = True

            # Safety break to prevent infinite loops
            if self.turn_count >= self.max_turns:
                logger.info("Reached max turn limit, ending game.")
                self.game_over = True

        logger.info("\nGame Over!")
        self.announce_winner()

    def announce_winner(self):
        """logger.info the winner(s)."""
        surviving_players = [p for p in self.players if p.money >= 0]
        if len(surviving_players) == 1:
            logger.info(f"The winner is {surviving_players[0].name} with ${surviving_players[0].money}!")
        else:
            # Could be multiple if time limit reached
            logger.info("Game ended with multiple survivors:")
            for p in surviving_players:
                logger.info(f" - {p.name} has ${p.money}")

# --------------------------------------------------------
# 3. Example Usage
# --------------------------------------------------------

if __name__ == "__main__":
    # Example: 4 players
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    game = MonopolyGame(player_names)
    game.run_game()