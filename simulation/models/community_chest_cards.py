from typing import List
from models.cards import Card

COMMUNITY_CHEST_CARDS = [
    Card(
        description="Advance to Go (Collect $200)",
        action_type="move",
        move_to_position=0  # position of "Go"
    ),
    Card(
        description="Bank error in your favor — Collect $200",
        action_type="collect",
        amount=200
    ),
    Card(
        description="Doctor's fee — Pay $50",
        action_type="pay",
        amount=50
    ),
    Card(
        description="From sale of stock you get $50",
        action_type="collect",
        amount=50
    ),
    Card(
        description="Get Out of Jail Free — This card may be kept until needed or traded",
        action_type="jail_free",
        get_out_of_jail_free=True
    ),
    Card(
        description="Go to Jail — Go directly to Jail, do not pass Go, do not collect $200",
        action_type="move",
        send_to_jail=True
    ),
    Card(
        description="Grand Opera Night — Collect $50 from every player",
        action_type="collect",
        amount=50,
        collect_from_all_players=True
    ),
    Card(
        description="Holiday Fund matures — Receive $100",
        action_type="collect",
        amount=100
    ),
    Card(
        description="Income tax refund — Collect $20",
        action_type="collect",
        amount=20
    ),
    Card(
        description="It is your birthday — Collect $10 from every player",
        action_type="collect",
        amount=10,
        collect_from_all_players=True
    ),
    Card(
        description="Life insurance matures — Collect $100",
        action_type="collect",
        amount=100
    ),
    Card(
        description="Hospital fees — Pay $100",
        action_type="pay",
        amount=100
    ),
    Card(
        description="School fees — Pay $150",
        action_type="pay",
        amount=150
    ),
    Card(
        description="Receive Consultancy Fee — $25",
        action_type="collect",
        amount=25
    ),
    Card(
        description="You are assessed for street repairs: $40 per house, $115 per hotel",
        action_type="repairs",
        pay_per_house=40,
        pay_per_hotel=115
    ),
    Card(
        description="You have won second prize in a beauty contest — Collect $10",
        action_type="collect",
        amount=10
    )
]