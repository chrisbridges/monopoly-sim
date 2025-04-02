from dataclasses import dataclass
from typing import Optional

@dataclass
class Card:
    description: str
    action_type: str  # "move", "collect", "pay", "jail_free", "repairs"
    
    # Movement-related
    move_to_position: Optional[int] = None
    move_nearest_utility: Optional[bool] = False
    move_nearest_railroad: Optional[bool] = False
    send_to_jail: Optional[bool] = False

    # Money-related
    amount: Optional[int] = 0  # Positive for collect, negative for pay (or just interpret based on action_type)
    collect_from_all_players: Optional[bool] = False  # e.g. "Grand Opera Night", "It is your birthday"
    
    # Repairs-related
    pay_per_house: Optional[int] = 0
    pay_per_hotel: Optional[int] = 0

    # Jail-free
    get_out_of_jail_free: Optional[bool] = False