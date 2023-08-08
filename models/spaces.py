# Complete Monopoly board spaces with their names, types, and details (if any)
# TODO: any advantage in stripping this to just property names and programmatically adding all values on init?
spaces = [
    ("Go", "Go"),
    ("Mediterranean Avenue", "Property", {"purchase_price": 60, "base_rent": 2, "mortgage_value": 30}),
    ("Community Chest", "Community Chest"),
    ("Baltic Avenue", "Property", {"purchase_price": 80, "base_rent": 4, "mortgage_value": 40}),
    ("Income Tax", "Tax", {"tax_amount": 200}),
    ("Reading Railroad", "Railroad", {"purchase_price": 200}),
    ("Oriental Avenue", "Property", {"purchase_price": 100, "base_rent": 6, "mortgage_value": 50}),
    ("Chance", "Chance"),
    ("Vermont Avenue", "Property", {"purchase_price": 100, "base_rent": 6, "mortgage_value": 50}),
    ("Connecticut Avenue", "Property", {"purchase_price": 120, "base_rent": 8, "mortgage_value": 60}),
    ("Jail", "Jail"),
    ("St. Charles Place", "Property", {"purchase_price": 140, "base_rent": 10, "mortgage_value": 70}),
    ("Electric Company", "Utility", {"purchase_price": 150}),
    ("States Avenue", "Property", {"purchase_price": 140, "base_rent": 10, "mortgage_value": 70}),
    ("Virginia Avenue", "Property", {"purchase_price": 160, "base_rent": 12, "mortgage_value": 80}),
    ("Pennsylvania Railroad", "Railroad", {"purchase_price": 200}),
    ("St. James Place", "Property", {"purchase_price": 180, "base_rent": 14, "mortgage_value": 90}),
    ("Community Chest", "Community Chest"),
    ("Tennessee Avenue", "Property", {"purchase_price": 180, "base_rent": 14, "mortgage_value": 90}),
    ("New York Avenue", "Property", {"purchase_price": 200, "base_rent": 16, "mortgage_value": 100}),
    ("Free Parking", "Free Parking"),
    ("Kentucky Avenue", "Property", {"purchase_price": 220, "base_rent": 18, "mortgage_value": 110}),
    ("Chance", "Chance"),
    ("Indiana Avenue", "Property", {"purchase_price": 220, "base_rent": 18, "mortgage_value": 110}),
    ("Illinois Avenue", "Property", {"purchase_price": 240, "base_rent": 20, "mortgage_value": 120}),
    ("B. & O. Railroad", "Railroad", {"purchase_price": 200}),
    ("Atlantic Avenue", "Property", {"purchase_price": 260, "base_rent": 22, "mortgage_value": 130}),
    ("Ventnor Avenue", "Property", {"purchase_price": 260, "base_rent": 22, "mortgage_value": 130}),
    ("Water Works", "Utility", {"purchase_price": 150}),
    ("Marvin Gardens", "Property", {"purchase_price": 280, "base_rent": 24, "mortgage_value": 140}),
    ("Go to Jail", "Go to Jail"),
    ("Pacific Avenue", "Property", {"purchase_price": 300, "base_rent": 26, "mortgage_value": 150}),
    ("North Carolina Avenue", "Property", {"purchase_price": 300, "base_rent": 26, "mortgage_value": 150}),
    ("Community Chest", "Community Chest"),
    ("Pennsylvania Avenue", "Property", {"purchase_price": 320, "base_rent": 28, "mortgage_value": 160}),
    ("Short Line", "Railroad", {"purchase_price": 200}),
    ("Chance", "Chance"),
    ("Park Place", "Property", {"purchase_price": 350, "base_rent": 35, "mortgage_value": 175}),
    ("Luxury Tax", "Tax", {"tax_amount": 100}),
    ("Boardwalk", "Property", {"purchase_price": 400, "base_rent": 50, "mortgage_value": 200})
]

# rent value for each property
rent_values = {
    "Mediterranean Avenue": [10, 30, 90, 160, 250],
    "Baltic Avenue": [20, 60, 180, 320, 450],
    "Oriental Avenue": [30, 90, 270, 400, 550],
    "Vermont Avenue": [30, 90, 270, 400, 550],
    "Connecticut Avenue": [40, 100, 300, 450, 600],
    "St. Charles Place": [50, 150, 450, 625, 750],
    "States Avenue": [50, 150, 450, 625, 750],
    "Virginia Avenue": [60, 180, 500, 700, 900],
    "St. James Place": [70, 200, 550, 750, 950],
    "Tennessee Avenue": [70, 200, 550, 750, 950],
    "New York Avenue": [80, 220, 600, 800, 1000],
    "Kentucky Avenue": [90, 250, 700, 875, 1050],
    "Indiana Avenue": [90, 250, 700, 875, 1050],
    "Illinois Avenue": [100, 300, 750, 925, 1100],
    "Atlantic Avenue": [110, 330, 800, 975, 1150],
    "Ventnor Avenue": [110, 330, 800, 975, 1150],
    "Marvin Gardens": [120, 360, 850, 1025, 1200],
    "Pacific Avenue": [130, 390, 900, 1100, 1275],
    "North Carolina Avenue": [130, 390, 900, 1100, 1275],
    "Pennsylvania Avenue": [150, 450, 1000, 1200, 1400],
    "Park Place": [175, 500, 1100, 1300, 1500],
    "Boardwalk": [200, 600, 1400, 1700, 2000]
}


def add_rent_values_to_spaces():

# Add the rent information to the spaces list
    updated_spaces = []

    for space in spaces:
        if space[1] == "Property":
            property_name = space[0]
            if property_name in rent_values:
                rent_info = rent_values[property_name]
                rents = {
                    1: rent_info[0],
                    2: rent_info[1],
                    3: rent_info[2],
                    4: rent_info[3],
                    5: rent_info[4]  # 5 houses is equivalent to a hotel
                }
                updated_space = (space[0], space[1], {**space[2], "rents": rents})
                updated_spaces.append(updated_space)
            else:
                updated_spaces.append(space)
        else:
            updated_spaces.append(space)

    return updated_spaces
