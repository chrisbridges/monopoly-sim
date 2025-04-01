# game_engine/actions.py

import random
from models.board import Square
from models.player import Player
from models.square_types import SquareType

def handle_square(player, square, players):
    print(f"{player.name} landed on {square.name} ({square.type}).")
    if square.type == SquareType.PROPERTY:
        handle_property(player, square, players)
    elif square.type == SquareType.TAX:
        handle_tax(player, square)
    elif square.type == SquareType.CHANCE:
        handle_chance(player)
    elif square.type == SquareType.COMMUNITY_CHEST:
        handle_community_chest(player)
    elif square.type == SquareType.GO_TO_JAIL:
        send_to_jail(player)
    # Jail, free parking, etc., do nothing special

def handle_property(player, square, players):
    if square.owner is None:
        # Simplified "always buy if you can afford it"
        if player.money >= (square.price or 0):
            square.owner = player.name
            player.owned_properties.append(square.position)
            player.money -= square.price
            print(f"{player.name} bought {square.name} for ${square.price}. Money: {player.money}")
    else:
        # Pay rent
        if square.owner != player.name:
            rent_amount = calculate_rent(square)
            player.money -= rent_amount
            # Find owner
            for p in players:
                if p.name == square.owner:
                    p.money += rent_amount
                    break
            print(f"{player.name} paid ${rent_amount} in rent to {square.owner}. Money: {player.money}")

def calculate_rent(square):
    if square.rent and len(square.rent) > 0:
        return square.rent[0]
    # Simplified fallback
    return 25 if square.type in ("railroad", "utility") else 10

def handle_tax(player, square):
    tax_amount = square.price or 0
    player.money -= tax_amount
    print(f"{player.name} paid tax of ${tax_amount}. Money: {player.money}")

def handle_chance(player):
    amount = random.choice([50, -50])
    player.money += amount
    print(f"{player.name} drew Chance: {amount:+}. Money: {player.money}")

def handle_community_chest(player):
    amount = random.choice([100, -100])
    player.money += amount
    print(f"{player.name} drew Community Chest: {amount:+}. Money: {player.money}")

def send_to_jail(player):
    print(f"{player.name} goes to Jail!")
    player.position = 10
    player.in_jail = True
    player.jail_turns = 0

def handle_bankruptcy(player, board):
    print(f"{player.name} went bankrupt!")
    for pos in player.owned_properties:
        board[pos].owner = None
    player.owned_properties.clear()