# game_engine/movement.py
import random

def roll_and_move(player, board, logger):
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    logger.info(f"{player.name} rolls {dice_total}.")

    old_position = player.position
    new_position = (old_position + dice_total) % len(board)

    # Passing GO
    if new_position < old_position:
        player.money += 200
        logger.info(f"{player.name} passed GO! +$200. Money: {player.money}")

    player.position = new_position
    return dice_total