# game_engine/jail.py

from dataclasses import replace
from models.player import Player


def handle_jail_turn(player: Player):
    """Handle a turn for a player who is currently in jail."""
    if player.jail_turns < 2:
        new_jail_turns = player.jail_turns + 1
        print(f"{player.name} is in jail (turn {player.jail_turns}).")
        return replace(player, jail_turns=new_jail_turns)
    else:
        """Release from jail"""
        new_jail_status = False
        new_jail_turns = 0
        print(f"{player.name} is released from jail.")
        return replace(player, jail_turns=new_jail_turns, in_jail=new_jail_status)