# game_engine/game.py

import logging
from dataclasses import dataclass, replace
from typing import List

from models.board import create_monopoly_board
from models.player import Player
# Assume that actions, movement, and jail modules are reworked as pure functions.
from game_engine import actions
from game_engine import movement
from game_engine import jail

@dataclass(frozen=True)
class GameState:
    board: List  # list of Square objects
    players: List[Player]
    current_player_index: int
    game_over: bool
    turn_count: int
    max_turns: int = 1000

def initial_state(player_names: List[str]) -> GameState:
    return GameState(
        board=create_monopoly_board(),
        players=[Player(name) for name in player_names],
        current_player_index=0,
        game_over=False,
        turn_count=0,
        max_turns=1000
    )

def next_player(state: GameState) -> GameState:
    """Advance to the next non-bankrupt player."""
    idx = state.current_player_index
    num_players = len(state.players)
    new_idx = (idx + 1) % num_players
    # Skip bankrupt players:
    while state.players[new_idx].money < 0:
        new_idx = (new_idx + 1) % num_players
    return replace(state, current_player_index=new_idx)

def play_turn(state: GameState) -> GameState:
    """Process one turn and return an updated game state."""
    current_idx = state.current_player_index
    player = state.players[current_idx]

    # 1) If player is bankrupt, skip to next player.
    if player.is_bankrupt:
        return next_player(state)
    
    new_state = state

    # 2) If the player is in jail, handle jail.
    if player.in_jail:
        # Assume jail.handle_jail_turn returns a new Player state.
        new_player = jail.handle_jail_turn(player)
        # Update players list immutably:
        new_players = list(state.players)
        new_players[current_idx] = new_player
        new_state = replace(state, players=new_players)
        # If the player remains in jail, skip movement.
        if new_player.in_jail:
            return next_player(new_state)
        # Otherwise, update our player reference.
        player = new_player

    # 3) Move the player.
    # Assume movement.move returns a tuple (new_player, dice_total)
    moved_player, dice_total = movement.move(player, state.board)
    new_players = list(new_state.players)
    new_players[current_idx] = moved_player
    new_state = replace(new_state, players=new_players)
    
    # 4) Handle the square logic.
    square = new_state.board[moved_player.position]
    # Assume actions.handle_square returns an updated game state.
    new_state = actions.handle_square(new_state, moved_player, square)
    
    # 5) If the move caused bankruptcy, update state accordingly.
    if moved_player.money < 0:
        new_state = actions.handle_bankruptcy(new_state, moved_player)
    
    # (Optionally: reset doubles count, etc.)
    
    # 6) Advance to the next player.
    return next_player(new_state)

def run_game(state: GameState) -> GameState:
    """Run the game loop until an end condition is met."""
    current_state = state
    while not current_state.game_over:
        # Increment turn count.
        current_state = replace(current_state, turn_count=current_state.turn_count + 1)
        # Process a turn.
        current_state = play_turn(current_state)
        # Check for end conditions.
        active_count = sum(1 for p in current_state.players if p.money >= 0)
        if active_count <= 1 or current_state.turn_count >= current_state.max_turns:
            current_state = replace(current_state, game_over=True)
    return current_state

def announce_winner(state: GameState) -> str:
    """Return a message with the winner(s) based on the final state."""
    survivors = [p for p in state.players if p.money >= 0]
    if len(survivors) == 1:
        return f"The winner is {survivors[0].name} with ${survivors[0].money}!"
    else:
        lines = ["Game ended with multiple survivors:"]
        lines += [f" - {p.name} has ${p.money}" for p in survivors]
        return "\n".join(lines)

# Main entry point for simulation:
if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    state = initial_state(player_names)
    print("Starting Monopoly game!")
    final_state = run_game(state)
    print("Game Over!")
    print(announce_winner(final_state))