# game_engine/actions.py

from ast import List
import random
from models.board import Square
from models.player import Player
from models.square_types import SquareType
from models.square import Chance, CommunityChest, GoToJail, Property, Tax

def handle_square(player: Player, square: Square, players: List[Player]):
    print(f"{player.name} landed on {square.name} ({square.type}).")
    if isinstance(square, Property):
        handle_property(player, square, players)
    elif isinstance(square, Tax):
        handle_tax(player, square)
    elif isinstance(square, Chance):
        handle_chance(player)
    elif isinstance(square, CommunityChest):
        handle_community_chest(player)
    elif isinstance(square, GoToJail):
        send_to_jail(player)
    # Jail, free parking, etc., do nothing special

def handle_property(player: Player, property: Property, players: List[Player]):
    if property.owner is None:
        # Simplified "always buy if you can afford it"
        if player.money >= (property.price or 0):
            property.owner = player.name
            player.owned_properties.append(property.position)
            player.money -= property.price
            print(f"{player.name} bought {property.name} for ${property.price}. Money: {player.money}")
    else:
        # Pay rent
        if property.owner != player.name:
            rent_amount = calculate_rent(property)
            player.money -= rent_amount
            # Find owner
            for p in players:
                if p.name == property.owner:
                    p.money += rent_amount
                    break
            print(f"{player.name} paid ${rent_amount} in rent to {property.owner}. Money: {player.money}")

def calculate_rent(square: Square):
    # TODO: add house and hotel logic
    if square.rent and len(square.rent) > 0:
        return square.rent[0]
    # TODO: implement railroad and utility logic
    return 25 if square.type in ("railroad", "utility") else 10

def handle_tax(player: Player, square: Square):
    # TODO: luxury tax is flat amount of $100
    # income tax is flat $200 or 10% of worth
    tax_amount = square.price or 0
    player.money -= tax_amount
    print(f"{player.name} paid tax of ${tax_amount}. Money: {player.money}")

def handle_chance(player: Player):
    # TODO: implement draw card logic
    amount = random.choice([50, -50])
    player.money += amount
    print(f"{player.name} drew Chance: {amount:+}. Money: {player.money}")

def handle_community_chest(player: Player):
    # TODO: implement draw card logic
    amount = random.choice([100, -100])
    player.money += amount
    print(f"{player.name} drew Community Chest: {amount:+}. Money: {player.money}")

def send_to_jail(player: Player):
    print(f"{player.name} goes to Jail!")
    player.position = 10
    player.in_jail = True
    player.jail_turns = 0

def handle_bankruptcy(player: Player, board):
    print(f"{player.name} went bankrupt!")
    # TODO: bankrupter gets all of bankrupty's properties
    for pos in player.owned_properties:
        board[pos].owner = None
    player.owned_properties.clear()