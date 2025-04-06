# chance_card_actions.py

from dataclasses import replace
from typing import List
from game_engine.game import GameState  # your immutable game state
from models.player import Player
from models.cards import Card
from models.card_action_types import CardActionTypes

# --- Dispatcher function ---

def apply_chance_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Given a chance card, dispatch to the proper action handler and return an updated game state.
    """
    if card.action_type == CardActionTypes.MOVE:
        return apply_move_card(state, player, card)
    elif card.action_type == CardActionTypes.COLLECT:
        return apply_collect_card(state, player, card)
    elif card.action_type == CardActionTypes.PAY:
        return apply_pay_card(state, player, card)
    elif card.action_type == CardActionTypes.JAIL_FREE:
        return apply_jail_free_card(state, player, card)
    elif card.action_type == CardActionTypes.REPAIRS:
        return apply_repairs_card(state, player, card)
    else:
        # Unknown card action; return state unchanged.
        return state

# --- MOVE Card Handlers ---

def apply_move_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Process a MOVE type chance card.
    This covers cards that instruct a player to move to a specific position,
    move to the nearest utility or railroad, move backward, or go to jail.
    """
    # Example 1: Direct move to a fixed position.
    if card.move_to_position is not None:
        # Optionally, if passing GO, add money. Assume move_player_directly handles that.
        return move_player_directly(state, player, card.move_to_position)
    
    # Example 2: Send player to jail.
    if getattr(card, 'send_to_jail', False):
        return send_player_to_jail(state, player)
    
    # Example 3: Move to nearest utility.
    if getattr(card, 'move_nearest_utility', False):
        return move_player_to_nearest_utility(state, player)
    
    # Example 4: Move to nearest railroad.
    if getattr(card, 'move_nearest_railroad', False):
        return move_player_to_nearest_railroad(state, player)
    
    # Example 5: Relative move (like "Go Back 3 Spaces"). If you add a field for relative movement:
    if hasattr(card, 'move_relative') and card.move_relative is not None:
        return move_player_relative(state, player, card.move_relative)
    
    return state

# --- COLLECT Card Handler ---

def apply_collect_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Process a COLLECT chance card.
    For a simple card, add card.amount to the player's money.
    """
    
    new_player = replace(player, money=player.money + card.amount)
    return update_player_in_state(state, new_player)

# --- PAY Card Handler ---

def apply_pay_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Process a PAY chance card.
    Deduct card.amount from the player's money.
    (If the card requires paying other players, that logic can be added here.)
    """
    
    new_player = replace(player, money=player.money - card.amount)
    return update_player_in_state(state, new_player)

# --- JAIL_FREE Card Handler ---

def apply_jail_free_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Process the Get Out of Jail Free card.
    Mark the player as having a Get Out of Jail Free card.
    """
    
    new_player = replace(player, has_get_out_of_jail_free_card=True)
    return update_player_in_state(state, new_player)

# --- REPAIRS Card Handler ---

def apply_repairs_card(state: GameState, player: Player, card: Card) -> GameState:
    """
    Process the Repairs card.
    Calculate the total repair cost based on properties owned by the player.
    (Assume we have a helper that calculates this by scanning the board.)
    """
    total_cost = calculate_total_repairs_cost(state, player, card.pay_per_house, card.pay_per_hotel)
    
    new_player = replace(player, money=player.money - total_cost)
    return update_player_in_state(state, new_player)

# --- Helper Functions ---

def update_player_in_state(state: GameState, new_player: Player) -> GameState:
    """
    Returns a new GameState with the specified player updated.
    """
    new_players = list(state.players)
    idx = next(i for i, p in enumerate(state.players) if p.name == new_player.name)
    new_players[idx] = new_player
    
    return replace(state, players=new_players)

def move_player_directly(state: GameState, player: Player, position: int) -> GameState:
    """
    Returns a new state with the player moved directly to the given position.
    (Assumes that any passing GO logic is handled within this function.)
    """
    
    new_player = replace(player, position=position)
    return update_player_in_state(state, new_player)

def send_player_to_jail(state: GameState, player: Player) -> GameState:
    """
    Returns a new state with the player sent to jail.
    (Assume jail is at position 10 and appropriate flags are set.)
    """
    
    new_player = replace(player, position=10, in_jail=True, jail_turns=0)
    return update_player_in_state(state, new_player)

def move_player_to_nearest_utility(state: GameState, player: Player) -> GameState:
    """
    Returns a new state with the player moved to the nearest utility.
    (Implementation similar to your previous lambda-based solution.)
    """
    # For brevity, assume this function is implemented.
    return state

def move_player_to_nearest_railroad(state: GameState, player: Player) -> GameState:
    """
    Returns a new state with the player moved to the nearest railroad.
    """
    # For brevity, assume this function is implemented.
    return state

def move_player_relative(state: GameState, player: Player, offset: int) -> GameState:
    """
    Returns a new state with the player moved relative to their current position.
    For example, if offset is -3, move the player 3 squares back.
    """
    
    board_length = len(state.board)
    new_position = (player.position + offset) % board_length
    new_player = replace(player, position=new_position)
    return update_player_in_state(state, new_player)

def calculate_total_repairs_cost(state: GameState, player: Player, cost_per_house: int, cost_per_hotel: int) -> int:
    """
    Calculate the total repair cost for the player by scanning the board for properties they own.
    Assumes that each property has a 'houses' attribute where 5 houses means a hotel.
    """
    total_cost = 0
    for square in state.board:
        if hasattr(square, 'owner') and square.owner == player.name and hasattr(square, 'houses'):
            if square.houses < 5:
                total_cost += square.houses * cost_per_house
            else:
                total_cost += cost_per_hotel
    return total_cost