import logging
from game_engine.game import MonopolyGame

logger = logging.getLogger(__name__)

# def ask_for_number_of_simulations():
# 	return input("How many games would you like to simulate? ")

if __name__ == "__main__":
	# games = int(ask_for_number_of_simulations())
	# Example: 4 players
	player_names = ["Alice", "Bob", "Charlie", "Diana"]
	game = MonopolyGame(player_names)
	for _ in range(10):
		print('game was run')
		game.run_game()