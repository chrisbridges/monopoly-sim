from dataclasses import dataclass
from typing import List
from models.square_types import SquareType

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
    price: int
    rent: List[int] # base rent, followed by rents for 1-5 houses
    color: str
    houses: int = 0 # 5 houses == hotel
    owner: str = None  # Name or ID of the owning player (None if unowned)
    is_mortgaged: bool = False

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
    price: int

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