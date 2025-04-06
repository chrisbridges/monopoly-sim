# game_engine/actions.py

from typing import List, Tuple
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
from game_engine.game import GameState

def handle_square(state: GameState, player: Player, square: Square) -> GameState:
    # TODO: these all need to be made to explicity return?
    print(f"{player.name} landed on {square.name}.")
    if isinstance(square, Property):
        return handle_property(state, player, square)
    elif isinstance(square, Tax):
        new_player = handle_tax(player, square)
        new_players = list(state.players)
        new_players[state.current_player_index] = new_player
        return replace(state, players=new_players)
    elif isinstance(square, Chance):
        draw_chance(player)
    elif isinstance(square, CommunityChest):
        draw_community_chest(player)
    elif isinstance(square, GoToJail):
        new_player = movement.send_to_jail(player)
        new_players = list(state.players)
        new_players[state.current_player_index] = new_player
        return replace(state, players=new_players)
    # Jail, free parking, etc., do nothing special

def handle_property(state: GameState, player: Player, property: Property) -> GameState:
    # If the property is unowned, attempt to purchase it:
    if property.owner is None:
        if player.money >= property.price:
            new_player, new_board = purchase_property(player, property, state.board)
            new_players = list(state.players)
            new_players[state.current_player_index] = new_player
            return replace(state, players=new_players, board=new_board)
        else:
            # Player cannot afford it; no change.
            return state
    else:
        # If the property is owned by someone else, handle rent payment.
        if property.owner != player.name:
            rent_amount = calculate_rent(property, property.owner, player)
            property_owner = find_property_owner(state, property)
            property_owner_idx = find_property_owner_idx(state, property)
            player_idx = state.current_player_index

            new_player = decrement_player_money(player, rent_amount)
            new_owner = increment_player_money(property_owner, rent_amount)
            
            # TODO: update current player index funcs and update other player
            new_players = list(state.players)
            new_players[player_idx] = new_player
            new_players[property_owner_idx] = new_owner

            return replace(state, players=new_players)
        else:
            # Landed on your own property; nothing to do.
            return state
        
def increment_player_money(player: Player, amount: int) -> Player:
    new_money = player.money + amount
    return replace(player, money=new_money)

def decrement_player_money(player: Player, amount: int) -> Player:
    new_money = player.money - amount
    return replace(player, money=new_money)
# TODO: combine this and the below func to return both player instance and index
def find_property_owner(state: GameState, property: Property) -> Player:
    """
    Find the owner of a property on the board.
    Returns the player instance who owns the property.
    """
    for player in state.players:
        if property.owner == player.name:
            return player

def find_property_owner_idx(state: GameState, property: Property) -> int:
    """
    Find the index of the player who owns a property on the board.
    Returns the index of the player in the players list.
    """
    for idx, player in enumerate(state.players):
        if property.owner == player.name:
            return idx

def purchase_property(player: Player, property: Property, board: List[Square]) -> Tuple[Player, List[Square]]:
    """
    Returns a new Player instance with money decremented,
    and a new board with the property updated so that its owner is the player's name.
    Ownership is indicated solely on the board via the property's 'owner' attribute.
    Assumes the player can afford the property.
    """
    new_player = decrement_player_money(player, property.price)

    # Update the board: replace the property with the new one.
    new_board = update_property_owner(property, player, board)

    return new_player, new_board

def update_property_owner(property: Property, owner: Player, board: List[Square]) -> List[Square]:
    """
    Update the property on the board with the new owner.
    """
    new_board = [
        replace(square, owner=property.owner) if isinstance(square, Property) and square.position == property.position else square
        for square in board
    ]
    return new_board

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

def handle_tax(player: Player, square: Tax) -> Player:
    """
    Handle the tax payment.
    """
    tax_amount = calculate_tax(player, square)
    new_player = decrement_player_money(player, tax_amount)

    # If the player goes bankrupt, handle that.
    # ideally catch higher up

    return new_player

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

def give_player_go_money(player: Player):
    return replace(player, money=player.money + CONSTANTS.GO_MONEY)