from dataclasses import dataclass, field
from typing import List

@dataclass
class Player:
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    has_get_out_of_jail_free_card: False # assume can only have 1 for now
    owned_properties: List[int] = field(default_factory=list)  # store board positions of owned squares