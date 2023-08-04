community_chest_cards = [
    {"description": "Advance to Go. (Collect $200)", "action": "move", "value": "Go"},
    {"description": "Bank error in your favor. Collect $200.", "action": "collect", "value": 200},
    {"description": "Doctor's fees. Pay $50.", "action": "pay", "value": 50},
    {"description": "Get out of jail free.", "action": "get_out_of_jail", "value": None},
    {"description": "Go to jail. Go directly to jail. Do not pass Go. Do not collect $200.", "action": "move", "value": "Jail"},
    {"description": "It is your birthday. Collect $10 from every player.", "action": "collect_from_each", "value": 10},
    {"description": "Grand Opera Night. Collect $50 from every player for opening night seats.", "action": "collect_from_each", "value": 50},
    {"description": "Income tax refund. Collect $20.", "action": "collect", "value": 20},
    {"description": "Life insurance matures. Collect $100.", "action": "collect", "value": 100},
    {"description": "Pay hospital fees of $100.", "action": "pay", "value": 100},
    {"description": "Pay school fees of $150.", "action": "pay", "value": 150},
    {"description": "Receive $25 consultancy fee.", "action": "collect", "value": 25},
    {"description": "You are assessed for street repairs. Pay $40 per house and $115 per hotel you own.", "action": "pay_per_house_hotel", "values": {"house": 40, "hotel": 115}},
    {"description": "You have won second prize in a beauty contest. Collect $10.", "action": "collect", "value": 10},
    {"description": "You inherit $100.", "action": "collect", "value": 100},
    {"description": "From sale of stock, you get $50.", "action": "collect", "value": 50}
]