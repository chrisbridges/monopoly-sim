def create_complete_monopoly_board():
    board = MonopolyBoard()
    
    # Complete Monopoly board spaces with their names, types, and details (if any)
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
    
    for space in spaces:
        board.add_space(*space)
    
    return board

board = create_complete_monopoly_board()

# Display the first 10 spaces for demonstration
display_first_n_spaces(board, 10)
