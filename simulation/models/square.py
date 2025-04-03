from dataclasses import dataclass
from typing import List
from models.square_types import SquareType
from simulation.models.constants import CONSTANTS

@dataclass
class Square:
    """
    Represents a square on the Monopoly board.
    """
    name: str
    position: int

@dataclass
class Go(Square):
    """
    Represents the 'Go' square on the Monopoly board.
    """
    name = "Go"
    position = 0

@dataclass
class Property(Square):
    """
    Represents a property square on the Monopoly board.
    """
    owner: str = None  # Name or ID of the owning player (None if unowned)
    price: int
    rent: List[int] # base rent, followed by rents for 1-5 houses
    color: str
    houses: int = 0 # 5 houses == hotel
    cost_per_house: int
    is_mortgaged: bool = False
    
    def get_property_value(self) -> int:
        # need to account if property is mortgaged
        if self.is_mortgaged:
            return self.price * CONSTANTS.MORTGAGE_DISCOUNT
        return self.price + (self.houses * self.cost_per_house)

@dataclass
class Railroad(Square):
    """
    Represents a railroad square on the Monopoly board.
    """
    price: int
    owner: str = None
    rent: List[int]
    is_mortgaged: bool = False

@dataclass
class CommunityChest(Square):
    """
    Represents a Community Chest square on the Monopoly board.
    """
    name = "Community Chest"
    position: int

@dataclass
class Chance(Square):
    """
    Represents a Chance square on the Monopoly board.
    """
    name = "Chance"
    position: int

@dataclass
class Tax(Square):
    """
    Represents a tax square on the Monopoly board.
    """
    name: str
    position: int
    tax: int

@dataclass
class Jail(Square):
    """
    Represents the Jail square on the Monopoly board.
    """
    name = "Jail / Just Visiting"
    position: int

@dataclass
class GoToJail(Square):
    """
    Represents the Go To Jail square on the Monopoly board.
    """
    name = "Go To Jail"

@dataclass
class Utility(Square):
    """
    Represents the utility square on the Monopoly board.
    """
    position: int
    price: int
    owner: str = None
    is_mortgaged: bool = False

@dataclass
class FreeParking(Square):
    """
    Represents the Free Parking square on the Monopoly board.
    """
    name = "Free Parking"
    position: int

