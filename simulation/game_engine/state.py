"""
Home of all state-modifying functions.
"""

from dataclasses import replace

from models.player import Player
from models.square import Property



def pay_rent(payer: Player, owner: Player, rent: int) -> (Player, Player):
    """
    Returns new Player instances for both payer and owner.
    """
    new_payer = replace(payer, money=payer.money - rent)
    new_owner = replace(owner, money=owner.money + rent)
    
    return new_payer, new_owner