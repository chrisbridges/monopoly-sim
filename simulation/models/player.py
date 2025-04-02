from dataclasses import dataclass, field
from typing import List

from models import board

@dataclass
class Player:
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    has_get_out_of_jail_free_card: bool = False # assume can only have 1 for now
    owned_properties: List[int] = field(default_factory=list)  # store board positions of owned squares
    net_worth: int = 0

    def calculate_net_worth(self):
        """
        Calculate the player's net worth based on their money and owned properties.
        For simplicity, we'll assume each property is worth its purchase price.
        """
        self.net_worth = self.money + sum(self.get_property_value(pos) for pos in self.owned_properties)

    def get_property_value(self, position: int) -> int:
        """
        Get the value of a property based on its position.
        This is a placeholder function. In a real game, you'd look up the property value from the board.
        """
        for property in board:
            if property.position == position:
                return property.price