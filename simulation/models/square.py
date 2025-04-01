from dataclasses import dataclass
from typing import List, Optional
from models.square_types import SquareType

@dataclass
class Square:
    name: str
    type: SquareType
    position: int
    price: Optional[int] = None
    rent: Optional[List[int]] = None
    color: Optional[str] = None
    owner: Optional[str] = None  # Name or ID of the owning player (None if unowned)
    houses: Optional[int] = 0
    is_mortgaged: Optional[bool] = False