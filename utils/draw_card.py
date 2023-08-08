import random

def draw_card(player, deck, board):
    """
    Draws a card from the specified deck (Community Chest or Chance) and applies its action to the player.
    """
    card = random.choice(deck)
    action = card["action"]
    value = card["value"]
    
    if action == "move":
        # Move to a specific space
        while player.current_position.name != value:
            player.current_position = board.traverse_board(1)
    elif action == "collect":
        player.receive_money(value)
    elif action == "pay":
        player.pay_money(value)
    elif action == "get_out_of_jail":
        player.get_out_of_jail_cards += 1
    elif action == "move_to_nearest":
        while value not in player.current_position.space_type:
            player.current_position = board.traverse_board(1)
            # after player reaches position, should be prompted either to buy it, auction it, or pay the owner rent (potentially a multiple in utility or railroad)
    elif action == "move_back":
        for _ in range(value):
            player.current_position = board.traverse_board(-1)  # Move back
    elif action == "pay_per_house_hotel":
        # TODO
        # In a real game, we'd loop through player's properties and count houses/hotels
        pass  # Placeholder
    
    return card["description"]

# Sample execution: Player1 draws a Community Chest card
drawn_card_description = draw_card(player1, community_chest_cards, board)
player1, drawn_card_description
