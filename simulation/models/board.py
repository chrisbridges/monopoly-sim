from typing import List
from models.square import Chance, CommunityChest, FreeParking, Go, GoToJail, Property, Railroad, Square, Tax, Utility
from models.square_types import SquareType
from models.property_colors import PropertyColors

def create_monopoly_board() -> List[Square]:
    """
    Returns a simplified Monopoly board. 
    Rents are from classic Monopoly for demonstration,
    but not all special logic (like railroads/utilities) is implemented here.
    """
    # TODO: need to add mortagage values for all properties
    board: List[Square] = [
        Go(),
        Property(name="Mediterranean Avenue", position=1, price=60, rent=[2, 10, 30, 90, 160, 250], color=PropertyColors.BROWN, houses=0, owner=None),
        CommunityChest(position=2),
        Property(name="Baltic Avenue", position=3, price=60, rent=[4, 20, 60, 180, 320, 450], color=PropertyColors.BROWN, houses=0, owner=None),
        Tax(name="Income Tax", position=4, price=200),  # We'll treat 'price' here as the tax amount - easier to make "rent"?
        Railroad(name="Reading Railroad", position=5, price=200, rent=[25,50,100,200], owner=None),
        Property(name="Oriental Avenue", position=6, price=100, rent=[6, 30, 90, 270, 400, 550], color=PropertyColors.LIGHT_BLUE, houses=0, owner=None),
        Chance(name="Chance", position=7),
        Property(name="Vermont Avenue", position=8, price=100, rent=[6, 30, 90, 270, 400, 550], color=PropertyColors.LIGHT_BLUE, houses=0, owner=None),
        Property(name="Connecticut Avenue", position=9, price=120, rent=[8, 40, 100, 300, 450, 600], color=PropertyColors.LIGHT_BLUE, houses=0, owner=None),
        Square(name="Jail / Just Visiting", position=10),
        Property(name="St. Charles Place", position=11, price=140, rent=[10, 50, 150, 450, 625, 750], color=PropertyColors.PINK, houses=0, owner=None),
        Utility(name="Electric Company", position=12, price=150),
        Property(name="States Avenue", position=13, price=140, rent=[10, 50, 150, 450, 625, 750], color=PropertyColors.PINK, houses=0, owner=None),
        Property(name="Virginia Avenue", position=14, price=160, rent=[12, 60, 180, 500, 700, 900], color=PropertyColors.PINK, houses=0, owner=None),
        Railroad(name="Pennsylvania Railroad", position=15, price=200, rent=[25,50,100,200], owner=None),
        Property(name="St. James Place", position=16, price=180, rent=[14, 70, 200, 550, 750, 950], color=PropertyColors.ORANGE, houses=0, owner=None),
        CommunityChest(position=17),
        Property(name="Tennessee Avenue", position=18, price=180, rent=[14, 70, 200, 550, 750, 950], color=PropertyColors.ORANGE, houses=0, owner=None),
        Property(name="New York Avenue", position=19, price=200, rent=[16, 80, 220, 600, 800, 1000], color=PropertyColors.ORANGE, houses=0, owner=None),
        FreeParking(position=20),
        Property(name="Kentucky Avenue", position=21, price=220, rent=[18, 90, 250, 700, 875, 1050], color=PropertyColors.RED, houses=0, owner=None),
        Chance(name="Chance", position=22),
        Property(name="Indiana Avenue", position=23, price=220, rent=[18, 90, 250, 700, 875, 1050], color=PropertyColors.RED, houses=0, owner=None),
        Property(name="Illinois Avenue", position=24, price=240, rent=[20, 100, 300, 750, 925, 1100], color=PropertyColors.RED, houses=0, owner=None),
        Railroad(name="B. & O. Railroad", position=25, price=200, rent=[25,50,100,200], owner=None),
        Property(name="Atlantic Avenue", position=26, price=260, rent=[22, 110, 330, 800, 975, 1150], color=PropertyColors.YELLOW, houses=0, owner=None),
        Property(name="Ventnor Avenue", position=27, price=260, rent=[22, 110, 330, 800, 975, 1150], color=PropertyColors.YELLOW, houses=0, owner=None),
        Utility(name="Water Works", position=28, price=150),
        Property(name="Marvin Gardens", position=29, price=280, rent=[24, 120, 360, 850, 1025, 1200], color=PropertyColors.YELLOW, houses=0, owner=None),
        GoToJail(position=30),
        Property(name="Pacific Avenue", position=31, price=300, rent=[26, 130, 390, 900, 1100, 1275], color=PropertyColors.GREEN, houses=0, owner=None),
        Property(name="North Carolina Avenue", position=32, price=300, rent=[26, 130, 390, 900, 1100, 1275], color=PropertyColors.GREEN, houses=0, owner=None),
        CommunityChest(position=33),
        Property(name="Pennsylvania Avenue", position=34, price=320, rent=[28, 150, 450, 1000, 1200, 1400], color=PropertyColors.GREEN, houses=0, owner=None),
        Railroad(name="Short Line Railroad", position=35, price=200, rent=[25,50,100,200], owner=None),
        Chance(name="Chance", position=36),
        Property(name="Park Place", position=37, price=350, rent=[35, 175, 500, 1100, 1300, 1500], color=PropertyColors.DARK_BLUE, houses=0, owner=None),
        Tax(name="Luxury Tax", position=38, price=100),
        Property(name="Boardwalk", position=39, price=400, rent=[50, 200, 600, 1400, 1700, 2000], color=PropertyColors.DARK_BLUE, houses=0, owner=None),
    ]

    return board