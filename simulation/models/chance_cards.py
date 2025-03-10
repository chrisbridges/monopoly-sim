from models.cards import Card


CHANCE_CARDS = [
    Card(
        description="Advance to Go (Collect $200)",
        action_type="move",
        move_to_position=0
        # You might handle the $200 as a separate rule for passing Go
    ),
    Card(
        description="Advance to Illinois Ave — If you pass Go, collect $200",
        action_type="move",
        move_to_position=24
    ),
    Card(
        description="Advance token to the nearest Utility. If unowned, buy it. If owned, pay 10x dice roll",
        action_type="move",
        move_nearest_utility=True
    ),
    Card(
        description="Advance token to the nearest Railroad. Pay owner twice the rental. If unowned, buy it",
        action_type="move",
        move_nearest_railroad=True
    ),
    Card(
        description="Bank pays you dividend of $50",
        action_type="collect",
        amount=50
    ),
    Card(
        description="Get Out of Jail Free — This card may be kept until needed or traded",
        action_type="jail_free",
        get_out_of_jail_free=True
    ),
    Card(
        description="Go Back 3 Spaces",
        action_type="move",
        # This might be handled differently (a negative dice move?), but you could do special logic
    ),
    Card(
        description="Go to Jail — Go directly to Jail, do not pass Go, do not collect $200",
        action_type="move",
        send_to_jail=True
    ),
    Card(
        description="Make General Repairs on All Your Property: For each house pay $25, for each hotel $100",
        action_type="repairs",
        pay_per_house=25,
        pay_per_hotel=100
    ),
    Card(
        description="Pay poor tax of $15",
        action_type="pay",
        amount=15
    ),
    Card(
        description="Take a trip to Reading Railroad — If you pass Go, collect $200",
        action_type="move",
        move_to_position=5  # position 5 is Reading Railroad
    ),
    Card(
        description="Take a walk on the Boardwalk — Advance token to Boardwalk",
        action_type="move",
        move_to_position=39
    ),
    Card(
        description="You have been elected Chairman of the Board — Pay each player $50",
        action_type="pay",
        amount=50
        # In practice, you'd handle distributing $50 to each other player
    ),
    Card(
        description="Your building loan matures — Collect $150",
        action_type="collect",
        amount=150
    ),
    Card(
        description="Advance to St. Charles Place — If you pass Go, collect $200",
        action_type="move",
        move_to_position=11
    ),
    Card(
        description="Speeding fine $15",
        action_type="pay",
        amount=15
    )
]