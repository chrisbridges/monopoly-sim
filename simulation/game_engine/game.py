# game_engine/game.py

import logging
from simulation.models.board import create_monopoly_board
from simulation.models.player import Player
from . import actions
from . import movement
from . import jail

logger = logging.getLogger(__name__)

class MonopolyGame:
    def __init__(self, player_names):
        self.board = create_monopoly_board()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.game_over = False
        self.turn_count = 0
        self.max_turns = 1000

    def play_turn(self):
        player = self.players[self.current_player_index]
        
        # 1) Check if player is bankrupt
        if player.money < 0:
            self.next_player()
            return
        
        # 2) If player is in jail, handle jail
        if player.in_jail:
            jail.handle_jail_turn(player, logger)
            # If still in jail, skip movement
            if player.in_jail:
                self.next_player()
                return
        
        # 3) Move the player
        dice_total = movement.roll_and_move(player, self.board, logger)
        
        # 4) Handle square logic
        square = self.board[player.position]
        actions.handle_square(player, square, self.players, logger)
        
        # 5) Check if player is bankrupt after the move
        if player.money < 0:
            actions.handle_bankruptcy(player, self.board, logger)
        
        # 6) Next player
        self.next_player()

    def next_player(self):
        """Advance to the next player who is still solvent."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        # Skip any players that are below 0 money
        while self.players[self.current_player_index].money < 0:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def run_game(self):
        logger.info("Starting Monopoly game!")
        while not self.game_over:
            self.turn_count += 1
            self.play_turn()

            # End condition
            active_count = sum(p.money >= 0 for p in self.players)
            if active_count <= 1 or self.turn_count >= self.max_turns:
                self.game_over = True

        logger.info("Game Over!")
        self.announce_winner()

    def announce_winner(self):
        survivors = [p for p in self.players if p.money >= 0]
        if len(survivors) == 1:
            logger.info(f"The winner is {survivors[0].name} with ${survivors[0].money}!")
        else:
            logger.info("Game ended with multiple survivors:")
            for p in survivors:
                logger.info(f" - {p.name} has ${p.money}")