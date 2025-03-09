from typing import List
from models.square import Square


def create_monopoly_board() -> List[Square]:
    """
    Returns a simplified Monopoly board. 
    Rents are from classic Monopoly for demonstration,
    but not all special logic (like railroads/utilities) is implemented here.
    """
    board = [
        Square(name="Go", type="go", position=0),
        Square(name="Mediterranean Avenue", type="property", position=1, price=60, rent=[2, 10, 30, 90, 160, 250], color="brown"),
        Square(name="Community Chest", type="community_chest", position=2),
        Square(name="Baltic Avenue", type="property", position=3, price=60, rent=[4, 20, 60, 180, 320, 450], color="brown"),
        Square(name="Income Tax", type="tax", position=4, price=200),  # We'll treat 'price' here as the tax amount
        Square(name="Reading Railroad", type="railroad", position=5, price=200),
        Square(name="Oriental Avenue", type="property", position=6, price=100, rent=[6, 30, 90, 270, 400, 550], color="light_blue"),
        Square(name="Chance", type="chance", position=7),
        Square(name="Vermont Avenue", type="property", position=8, price=100, rent=[6, 30, 90, 270, 400, 550], color="light_blue"),
        Square(name="Connecticut Avenue", type="property", position=9, price=120, rent=[8, 40, 100, 300, 450, 600], color="light_blue"),
        Square(name="Jail / Just Visiting", type="jail", position=10),
        Square(name="St. Charles Place", type="property", position=11, price=140, rent=[10, 50, 150, 450, 625, 750], color="pink"),
        Square(name="Electric Company", type="utility", position=12, price=150),
        Square(name="States Avenue", type="property", position=13, price=140, rent=[10, 50, 150, 450, 625, 750], color="pink"),
        Square(name="Virginia Avenue", type="property", position=14, price=160, rent=[12, 60, 180, 500, 700, 900], color="pink"),
        Square(name="Pennsylvania Railroad", type="railroad", position=15, price=200),
        Square(name="St. James Place", type="property", position=16, price=180, rent=[14, 70, 200, 550, 750, 950], color="orange"),
        Square(name="Community Chest", type="community_chest", position=17),
        Square(name="Tennessee Avenue", type="property", position=18, price=180, rent=[14, 70, 200, 550, 750, 950], color="orange"),
        Square(name="New York Avenue", type="property", position=19, price=200, rent=[16, 80, 220, 600, 800, 1000], color="orange"),
        Square(name="Free Parking", type="free_parking", position=20),
        Square(name="Kentucky Avenue", type="property", position=21, price=220, rent=[18, 90, 250, 700, 875, 1050], color="red"),
        Square(name="Chance", type="chance", position=22),
        Square(name="Indiana Avenue", type="property", position=23, price=220, rent=[18, 90, 250, 700, 875, 1050], color="red"),
        Square(name="Illinois Avenue", type="property", position=24, price=240, rent=[20, 100, 300, 750, 925, 1100], color="red"),
        Square(name="B. & O. Railroad", type="railroad", position=25, price=200),
        Square(name="Atlantic Avenue", type="property", position=26, price=260, rent=[22, 110, 330, 800, 975, 1150], color="yellow"),
        Square(name="Ventnor Avenue", type="property", position=27, price=260, rent=[22, 110, 330, 800, 975, 1150], color="yellow"),
        Square(name="Water Works", type="utility", position=28, price=150),
        Square(name="Marvin Gardens", type="property", position=29, price=280, rent=[24, 120, 360, 850, 1025, 1200], color="yellow"),
        Square(name="Go To Jail", type="go_to_jail", position=30),
        Square(name="Pacific Avenue", type="property", position=31, price=300, rent=[26, 130, 390, 900, 1100, 1275], color="green"),
        Square(name="North Carolina Avenue", type="property", position=32, price=300, rent=[26, 130, 390, 900, 1100, 1275], color="green"),
        Square(name="Community Chest", type="community_chest", position=33),
        Square(name="Pennsylvania Avenue", type="property", position=34, price=320, rent=[28, 150, 450, 1000, 1200, 1400], color="green"),
        Square(name="Short Line Railroad", type="railroad", position=35, price=200),
        Square(name="Chance", type="chance", position=36),
        Square(name="Park Place", type="property", position=37, price=350, rent=[35, 175, 500, 1100, 1300, 1500], color="dark_blue"),
        Square(name="Luxury Tax", type="tax", position=38, price=100),
        Square(name="Boardwalk", type="property", position=39, price=400, rent=[50, 200, 600, 1400, 1700, 2000], color="dark_blue"),
    ]
    return board