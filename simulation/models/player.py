from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Player:
    name: str
    money: int = 1500
    position: int = 0
    doubles_count: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    has_get_out_of_jail_free_card: bool = False
    is_bankrupt: bool = False

    def calculate_net_worth(self, board: List) -> int:
        """
        Calculate the player's net worth based on their money plus the value of properties they own.
        Ownership is determined by scanning the board: each square that has an 'owner' attribute matching
        the player's name contributes its value.
        
        Assumes that property squares have either a `get_property_value()` method or a `price` attribute.
        """
        property_value = 0
        for square in board:
            if hasattr(square, 'owner') and square.owner == self.name:
                if hasattr(square, 'get_property_value'):
                    property_value += square.get_property_value()
                elif hasattr(square, 'price'):
                    property_value += square.price
        return self.money + property_value