# game_engine/actions.py

from typing import List
import random
from dataclasses import replace
from models.constants import CONSTANTS
from models.board import Square
from models.player import Player
from models.square import Chance, CommunityChest, GoToJail, Property, Railroad, Tax, Utility
from game_engine import movement
from models.chance_cards import CHANCE_CARDS
from models.community_chest_cards import COMMUNITY_CHEST_CARDS
from game_engine import jail

def handle_square(player: Player, square: Square, players: List[Player]):
    print(f"{player.name} landed on {square.name}.")
    if isinstance(square, Property):
        handle_property(player, square, players)
    elif isinstance(square, Tax):
        calculate_tax(player, square)
    elif isinstance(square, Chance):
        draw_chance(player)
    elif isinstance(square, CommunityChest):
        draw_community_chest(player)
    elif isinstance(square, GoToJail):
        send_to_jail(player)
    # Jail, free parking, etc., do nothing special

def handle_property(player: Player, property: Property, players: List[Player]) -> None:
    # Check if property is owned
    if property.owner is None:
        # Simplified "always buy if you can afford it"
        if player.money >= (property.price or 0):
            # property.owner = player.name
            # player.owned_properties.append(property.position)
            # player.money -= property.price
            print(f"{player.name} bought {property.name} for ${property.price}. Money: {player.money}")
    else:
        # Pay rent
        if property.owner != player.name:
            rent_amount = calculate_rent(property, property.owner, player)
            # player.money -= rent_amount
            # Find owner
            for p in players:
                if p.name == property.owner:
                    # p.money += rent_amount
                    break
            print(f"{player.name} paid ${rent_amount} in rent to {property.owner}. Money: {player.money}")

# TODO: extract all rent funcs into own file
def calculate_rent(property: Property, property_owner: Player) -> int:
    if isinstance(property, Utility):
        return calculate_utility_rent(property_owner)

    elif isinstance(property, Railroad):
        return calculate_railroad_rent(property_owner, property)

    elif isinstance(property, Property):
        return calculate_property_rent(property)

def calculate_utility_rent(property_owner) -> int:
    # instead of passing in player's dice roll, rolling once more for now
    dice_roll = movement.roll_dice()
    utilities_owned = check_if_same_player_owns_both_utilities(property_owner)
    utility_multiplier = get_utility_multiplier(utilities_owned)
    utility_rent = dice_roll * utility_multiplier

    return utility_rent

def calculate_railroad_rent(property_owner, railroad) -> int:
    number_of_railroads_owned = check_number_of_railroads_owned(property_owner)
    railroad_rent = railroad.rent[number_of_railroads_owned]

    return railroad_rent

def calculate_property_rent(property) -> int:
    # 0 houses == base rent, 5 houses == hotel
    return property.rent[property.houses]

def calculate_tax(player: Player, square: Tax) -> int:
    """
    Income tax can vary, luxury tax always flat.
    """
    if property.name == "Income Tax":
        player_net_worth = player.calculate_net_worth()
        return min(200, player_net_worth * 0.1)
    else:
        return square.tax

def draw_chance():
    number_of_chance_cards = len(CHANCE_CARDS)
    random_index = random.randrange(number_of_chance_cards)

    return CHANCE_CARDS[random_index]

def draw_community_chest(player: Player):
    number_of_community_chest_cards = len(COMMUNITY_CHEST_CARDS)
    random_index = random.randrange(number_of_community_chest_cards)

    return COMMUNITY_CHEST_CARDS[random_index]

def send_to_jail(player: Player) -> Player:
    print(f"{player.name} goes to Jail!")
    return replace(player, 
                   in_jail=True, 
                   position=CONSTANTS.JAIL_POSITION, 
                   jail_turns=0, 
                   doubles_count=0)


def handle_bankruptcy(player: Player, board):
    print(f"{player.name} went bankrupt!")
    # TODO: bankrupter gets all of bankrupty's properties
    # houses get sold back to bank at half price
    for pos in player.owned_properties:
        board[pos].owner = None
    player.owned_properties.clear()

def check_if_same_player_owns_both_utilities(property_owner: Player) -> bool:
    """
    Check if the same player owns both utilities.
    """
    utility_counter = 0
    for property in property_owner:
        if isinstance(property, Utility):
            utility_counter += 1

    return True if utility_counter == 2 else False

def get_utility_multiplier(utilities_owned: int) -> int:
    """
    Get the utility multiplier based on the number of utilities owned.
    """
    if utilities_owned == 1:
        return 4
    elif utilities_owned == 2:
        return 10
    
def check_number_of_railroads_owned(property_owner: Player) -> int:
    """
    Check how many railroads the player owns.
    """
    railroad_counter = 0
    for property in property_owner:
        if isinstance(property, Railroad):
            railroad_counter += 1

    return railroad_counter
