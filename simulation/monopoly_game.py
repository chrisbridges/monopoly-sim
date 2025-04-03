from game_engine.game import MonopolyGame

if __name__ == "__main__":
	# Example: 4 players
	player_names = ["Alice", "Bob", "Charlie", "Diana"]
	game = MonopolyGame(player_names)
	# for _ in range(1):
	print('game was run')
	game.run_game()