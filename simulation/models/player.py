from dataclasses import dataclass, field
from typing import List, Union

from models import board
from models.square import Property, Railroad, Utility

@dataclass
class Player:
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    has_get_out_of_jail_free_card: bool = False # assume can only have 1 for now
    owned_properties: List[Property] = field(default_factory=list)  # store board positions of owned squares
    # net_worth: int = 0

    def calculate_net_worth(self) -> int:
        """
        Calculate the player's net worth based on their money and owned properties.
        Across the game, values are equivalent to their purchase price, unless mortgaged.
        """
        value_of_properties_and_houses = 0

        for property in self.owned_properties:
            if isinstance(property, Property):
                value_of_properties_and_houses += property.get_property_value()
            elif isinstance(property, Railroad):
                value_of_properties_and_houses += property.price
            elif isinstance(property, Utility):
                value_of_properties_and_houses += property.price
        
        return self.money + value_of_properties_and_houses