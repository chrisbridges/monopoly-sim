"""
Home of all state-modifying functions.
"""

from dataclasses import replace

from models.player import Player
from models.square import Property

def purchase_property(player: Player, property: Property) -> Player:
    """
    Returns a new Player instance reflecting the purchase.
    Assumes player can afford the property.
    """
    new_money = player.money - property.price
    new_owned = player.owned_properties + [property]
    # Using `replace` from dataclasses to create a copy with modifications.
    # TODO: need to modify property owner too? or keep out of that class
    return replace(player, money=new_money, owned_properties=new_owned)

def pay_rent(payer: Player, owner: Player, rent: int) -> (Player, Player):
    """
    Returns new Player instances for both payer and owner.
    """
    new_payer = replace(payer, money=payer.money - rent)
    new_owner = replace(owner, money=owner.money + rent)
    
    return new_payer, new_owner