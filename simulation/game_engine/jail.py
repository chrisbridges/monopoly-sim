# game_engine/jail.py

from models.player import Player


def handle_jail_turn(player: Player):
    """Handle a turn for a player who is currently in jail."""
    if player.jail_turns < 2:
        player.jail_turns += 1
        print(f"{player.name} is in jail (turn {player.jail_turns}).")
    else:
        player.in_jail = False
        player.jail_turns = 0
        print(f"{player.name} is released from jail.")