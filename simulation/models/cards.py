from dataclasses import dataclass
from typing import Optional

@dataclass
class Card:
    description: str
    action_type: str  # "move", "collect", "pay", "jail_free", "repairs"
    
    # Movement-related
    move_to_position: Optional[int] = None
    move_nearest_utility: bool = False
    move_nearest_railroad: bool = False
    send_to_jail: bool = False

    # Money-related
    amount: int = 0  # Positive for collect, negative for pay (or just interpret based on action_type)
    collect_from_all_players: bool = False  # e.g. "Grand Opera Night", "It is your birthday"
    
    # Repairs-related
    pay_per_house: int = 0
    pay_per_hotel: int = 0

    # Jail-free
    get_out_of_jail_free: bool = False