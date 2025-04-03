from models.cards import Card
from simulation.models.card_action_types import CardActionTypes

CHANCE_CARDS = [
    Card(
        description="Advance to Go (Collect $200)",
        action_type=CardActionTypes.MOVE,
        move_to_position=0
        # TODO: add amount to collect
    ),
    Card(
        description="Advance to Illinois Ave — If you pass Go, collect $200",
        action_type=CardActionTypes.MOVE,
        move_to_position=24
    ),
    Card(
        description="Advance token to the nearest Utility. If unowned, buy it. If owned, pay 10x dice roll",
        action_type=CardActionTypes.MOVE,
        move_nearest_utility=True
    ),
    Card(
        description="Advance token to the nearest Railroad. Pay owner twice the rental. If unowned, buy it",
        action_type=CardActionTypes.MOVE,
        move_nearest_railroad=True
    ),
    Card(
        description="Bank pays you dividend of $50",
        action_type=CardActionTypes.COLLECT,
        amount=50
    ),
    Card(
        description="Get Out of Jail Free — This card may be kept until needed or traded",
        action_type=CardActionTypes.JAIL_FREE,
        get_out_of_jail_free=True
    ),
    Card(
        description="Go Back 3 Spaces",
        action_type=CardActionTypes.MOVE,
        # TODO: handle change player position
        # This might be handled differently (a negative dice move?), but you could do special logic
    ),
    Card(
        description="Go to Jail — Go directly to Jail, do not pass Go, do not collect $200",
        action_type=CardActionTypes.MOVE,
        send_to_jail=True
    ),
    Card(
        description="Make General Repairs on All Your Property: For each house pay $25, for each hotel $100",
        action_type=CardActionTypes.REPAIRS,
        pay_per_house=25,
        pay_per_hotel=100
    ),
    Card(
        description="Pay poor tax of $15",
        action_type=CardActionTypes.PAY,
        amount=15
    ),
    Card(
        description="Take a trip to Reading Railroad — If you pass Go, collect $200",
        action_type=CardActionTypes.MOVE,
        move_to_position=5  # position 5 is Reading Railroad
    ),
    Card(
        description="Take a walk on the Boardwalk — Advance token to Boardwalk",
        action_type=CardActionTypes.MOVE,
        move_to_position=39
    ),
    Card(
        description="You have been elected Chairman of the Board — Pay each player $50",
        action_type=CardActionTypes.PAY,
        amount=50
        # TODO: In practice, you'd handle distributing $50 to each other player
    ),
    Card(
        description="Your building loan matures — Collect $150",
        action_type=CardActionTypes.COLLECT,
        amount=150
    ),
    Card(
        description="Advance to St. Charles Place — If you pass Go, collect $200",
        action_type=CardActionTypes.MOVE,
        move_to_position=11
    ),
    Card(
        description="Speeding fine $15",
        action_type=CardActionTypes.PAY,
        amount=15
    )
]