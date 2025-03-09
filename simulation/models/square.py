from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Square:
    name: str
    type: str  # e.g. "property", "railroad", "utility", "tax", "chance", "community_chest", "jail", "go", "free_parking", "go_to_jail"
    position: int
    price: Optional[int] = None
    rent: Optional[List[int]] = None
    color: Optional[str] = None
    owner: Optional[str] = None  # Name or ID of the owning player (None if unowned)