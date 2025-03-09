import logging
from game_engine.game import MonopolyGame

logger = logging.getLogger(__name__)

if __name__ == "__main__":
	# Example: 4 players
	player_names = ["Alice", "Bob", "Charlie", "Diana"]
	game = MonopolyGame(player_names)
	print('game was run')
	for _ in range(100):
		game.run_game()