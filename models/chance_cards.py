chance_cards = [
    {"description": "Advance to Go. (Collect $200)", "action": "move", "value": "Go"},
    {"description": "Advance to Illinois Ave.", "action": "move", "value": "Illinois Avenue"},
    {"description": "Advance token to nearest Utility.", "action": "move_to_nearest", "value": "Utility"},
    {"description": "Advance token to the nearest Railroad.", "action": "move_to_nearest", "value": "Railroad"},
    {"description": "Advance to St. Charles Place.", "action": "move", "value": "St. Charles Place"},
    {"description": "Bank pays you dividend of $50.", "action": "collect", "value": 50},
    {"description": "Get out of jail free.", "action": "get_out_of_jail", "value": None},
    {"description": "Go back three spaces.", "action": "move_back", "value": 3},
    {"description": "Go directly to jail. Do not pass Go. Do not collect $200.", "action": "move", "value": "Jail"},
    {"description": "Make general repairs on all your properties. Pay $25 for each house and $100 for each hotel.", "action": "pay_per_house_hotel", "values": {"house": 25, "hotel": 100}},
    {"description": "Pay poor tax of $15.", "action": "pay", "value": 15},
    {"description": "Take a trip to Reading Railroad.", "action": "move", "value": "Reading Railroad"},
    {"description": "Take a walk on the Boardwalk.", "action": "move", "value": "Boardwalk"},
    {"description": "You have been elected Chairman of the Board. Pay each player $50.", "action": "pay_each", "value": 50},
    {"description": "Your building and loan matures. Collect $150.", "action": "collect", "value": 150},
    {"description": "You have won a crossword competition. Collect $100.", "action": "collect", "value": 100}
]

community_chest_cards[:3], chance_cards[:3]  # Display the first 3 cards of each type for demonstration
