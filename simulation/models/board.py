from typing import List
from models.square import Square
from models.square_types import SquareType
from models.property_colors import PropertyColors

def create_monopoly_board() -> List[Square]:
    """
    Returns a simplified Monopoly board. 
    Rents are from classic Monopoly for demonstration,
    but not all special logic (like railroads/utilities) is implemented here.
    """
    board = [
        Square(name="Go", type=SquareType.GO, position=0),
        Square(name="Mediterranean Avenue", type=SquareType.PROPERTY, position=1, price=60, rent=[2, 10, 30, 90, 160, 250], color=PropertyColors.BROWN),
        Square(name="Community Chest", type=SquareType.COMMUNITY_CHEST, position=2),
        Square(name="Baltic Avenue", type=SquareType.PROPERTY, position=3, price=60, rent=[4, 20, 60, 180, 320, 450], color=PropertyColors.BROWN),
        Square(name="Income Tax", type=SquareType.TAX, position=4, price=200),  # We'll treat 'price' here as the tax amount
        Square(name="Reading Railroad", type=SquareType.RAILROAD, position=5, price=200),
        Square(name="Oriental Avenue", type=SquareType.PROPERTY, position=6, price=100, rent=[6, 30, 90, 270, 400, 550], color=PropertyColors.LIGHT_BLUE),
        Square(name="Chance", type=SquareType.CHANCE, position=7),
        Square(name="Vermont Avenue", type=SquareType.PROPERTY, position=8, price=100, rent=[6, 30, 90, 270, 400, 550], color=PropertyColors.LIGHT_BLUE),
        Square(name="Connecticut Avenue", type=SquareType.PROPERTY, position=9, price=120, rent=[8, 40, 100, 300, 450, 600], color=PropertyColors.LIGHT_BLUE),
        Square(name="Jail / Just Visiting", type=SquareType.JAIL, position=10),
        Square(name="St. Charles Place", type=SquareType.PROPERTY, position=11, price=140, rent=[10, 50, 150, 450, 625, 750], color=PropertyColors.PINK),
        Square(name="Electric Company", type=SquareType.UTILITY, position=12, price=150),
        Square(name="States Avenue", type=SquareType.PROPERTY, position=13, price=140, rent=[10, 50, 150, 450, 625, 750], color=PropertyColors.PINK),
        Square(name="Virginia Avenue", type=SquareType.PROPERTY, position=14, price=160, rent=[12, 60, 180, 500, 700, 900], color=PropertyColors.PINK),
        Square(name="Pennsylvania Railroad", type=SquareType.RAILROAD, position=15, price=200),
        Square(name="St. James Place", type=SquareType.PROPERTY, position=16, price=180, rent=[14, 70, 200, 550, 750, 950], color=PropertyColors.ORANGE),
        Square(name="Community Chest", type=SquareType.COMMUNITY_CHEST, position=17),
        Square(name="Tennessee Avenue", type=SquareType.PROPERTY, position=18, price=180, rent=[14, 70, 200, 550, 750, 950], color=PropertyColors.ORANGE),
        Square(name="New York Avenue", type=SquareType.PROPERTY, position=19, price=200, rent=[16, 80, 220, 600, 800, 1000], color=PropertyColors.ORANGE),
        Square(name="Free Parking", type=SquareType.FREE_PARKING, position=20),
        Square(name="Kentucky Avenue", type=SquareType.PROPERTY, position=21, price=220, rent=[18, 90, 250, 700, 875, 1050], color=PropertyColors.RED),
        Square(name="Chance", type=SquareType.CHANCE, position=22),
        Square(name="Indiana Avenue", type=SquareType.PROPERTY, position=23, price=220, rent=[18, 90, 250, 700, 875, 1050], color=PropertyColors.RED),
        Square(name="Illinois Avenue", type=SquareType.PROPERTY, position=24, price=240, rent=[20, 100, 300, 750, 925, 1100], color=PropertyColors.RED),
        Square(name="B. & O. Railroad", type=SquareType.RAILROAD, position=25, price=200),
        Square(name="Atlantic Avenue", type=SquareType.PROPERTY, position=26, price=260, rent=[22, 110, 330, 800, 975, 1150], color=PropertyColors.YELLOW),
        Square(name="Ventnor Avenue", type=SquareType.PROPERTY, position=27, price=260, rent=[22, 110, 330, 800, 975, 1150], color=PropertyColors.YELLOW),
        Square(name="Water Works", type=SquareType.UTILITY, position=28, price=150),
        Square(name="Marvin Gardens", type=SquareType.PROPERTY, position=29, price=280, rent=[24, 120, 360, 850, 1025, 1200], color=PropertyColors.YELLOW),
        Square(name="Go To Jail", type=SquareType.GO_TO_JAIL, position=30),
        Square(name="Pacific Avenue", type=SquareType.PROPERTY, position=31, price=300, rent=[26, 130, 390, 900, 1100, 1275], color=PropertyColors.GREEN),
        Square(name="North Carolina Avenue", type=SquareType.PROPERTY, position=32, price=300, rent=[26, 130, 390, 900, 1100, 1275], color=PropertyColors.GREEN),
        Square(name="Community Chest", type=SquareType.COMMUNITY_CHEST, position=33),
        Square(name="Pennsylvania Avenue", type=SquareType.PROPERTY, position=34, price=320, rent=[28, 150, 450, 1000, 1200, 1400], color=PropertyColors.GREEN),
        Square(name="Short Line Railroad", type=SquareType.RAILROAD, position=35, price=200),
        Square(name="Chance", type=SquareType.CHANCE, position=36),
        Square(name="Park Place", type=SquareType.PROPERTY, position=37, price=350, rent=[35, 175, 500, 1100, 1300, 1500], color=PropertyColors.DARK_BLUE),
        Square(name="Luxury Tax", type=SquareType.TAX, position=38, price=100),
        Square(name="Boardwalk", type=SquareType.PROPERTY, position=39, price=400, rent=[50, 200, 600, 1400, 1700, 2000], color=PropertyColors.DARK_BLUE),
    ]
    return board