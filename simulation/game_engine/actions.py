# game_engine/actions.py

import random
from models.board import Square
from models.player import Player

def handle_square(player, square, players, logger):
    logger.info(f"{player.name} landed on {square.name} ({square.type}).")
    if square.type == "property":
        handle_property(player, square, players, logger)
    elif square.type == "tax":
        handle_tax(player, square, logger)
    elif square.type == "chance":
        handle_chance(player, logger)
    elif square.type == "community_chest":
        handle_community_chest(player, logger)
    elif square.type == "go_to_jail":
        send_to_jail(player, logger)
    # Jail, free parking, etc., do nothing special

def handle_property(player, square, players, logger):
    if square.owner is None:
        # Simplified "always buy if you can afford it"
        if player.money >= (square.price or 0):
            square.owner = player.name
            player.owned_properties.append(square.position)
            player.money -= square.price
            logger.info(f"{player.name} bought {square.name} for ${square.price}. Money: {player.money}")
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
            logger.info(f"{player.name} paid ${rent_amount} in rent to {square.owner}. Money: {player.money}")

def calculate_rent(square):
    if square.rent and len(square.rent) > 0:
        return square.rent[0]
    # Simplified fallback
    return 25 if square.type in ("railroad", "utility") else 10

def handle_tax(player, square, logger):
    tax_amount = square.price or 0
    player.money -= tax_amount
    logger.info(f"{player.name} paid tax of ${tax_amount}. Money: {player.money}")

def handle_chance(player, logger):
    amount = random.choice([50, -50])
    player.money += amount
    logger.info(f"{player.name} drew Chance: {amount:+}. Money: {player.money}")

def handle_community_chest(player, logger):
    amount = random.choice([100, -100])
    player.money += amount
    logger.info(f"{player.name} drew Community Chest: {amount:+}. Money: {player.money}")

def send_to_jail(player, logger):
    logger.info(f"{player.name} goes to Jail!")
    player.position = 10
    player.in_jail = True
    player.jail_turns = 0

def handle_bankruptcy(player, board, logger):
    logger.info(f"{player.name} went bankrupt!")
    for pos in player.owned_properties:
        board[pos].owner = None
    player.owned_properties.clear()