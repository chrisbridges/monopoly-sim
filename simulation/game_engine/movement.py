import random
from dataclasses import replace
from typing import List, Tuple
from models.player import Player
from models.square import Square
from game_engine import actions
from models.constants import CONSTANTS

def roll_dice() -> Tuple[int, int]:
    """Roll two dice and return their values."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def move(player: Player) -> Player:
    """
    Pure function that simulates rolling dice and moving the player.
    Returns a new Player state and the dice total.
    
    - Updates doubles_count: if the player rolled doubles, increments the count; otherwise resets it.
    - Updates position based on dice roll.
    - If the player passes GO (i.e. new position is numerically lower than old position), adds $200.
    """
    dice1, dice2 = roll_dice()
    total = dice1 + dice2
    rolled_doubles = (dice1 == dice2)
    
    # Update doubles_count: increment if doubles, otherwise reset to 0.
    new_doubles_count = player.doubles_count + 1 if rolled_doubles else 0

    if new_doubles_count == 3:
        return actions.send_to_jail(player)

    old_position = player.position
    new_position = (old_position + total) % CONSTANTS.BOARD_LENGTH
    
    # Handle passing GO: if new position is "before" the old one, add $200.
    new_money = player.money
    if new_position < old_position:
        new_money += 200

    # Create a new Player with updated state.
    return replace(player,
                    money=new_money,
                    position=new_position,
                    doubles_count=new_doubles_count)

def advance_to_go(player: Player) -> Player:
    """
    Move the player directly to GO and collect $200.
    This is a special case for certain cards or squares.
    """
    return replace(player, position=0, money=player.money + 200)

def send_to_jail(player: Player) -> Player:
    print(f"{player.name} goes to Jail!")
    return replace(player, 
                   in_jail=True, 
                   position=CONSTANTS.JAIL_POSITION, 
                   jail_turns=0, 
                   doubles_count=0)