from board_space import BoardSpace

class MonopolyBoard:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_space(self, name, space_type, details=None):
        new_space = BoardSpace(name, space_type, details)
        if not self.head:
            self.head = new_space
            self.tail = new_space
            self.tail.next_space = self.head  # Making it circular
        else:
            self.tail.next_space = new_space
            self.tail = new_space
            self.tail.next_space = self.head  # Making it circular

    def traverse_board(self, steps):
        # This function will simulate a player's movement on the board
        # TODO: does this properly traverse moving backwards?
        current = self.head
        for _ in range(steps):
            current = current.next_space
        return current.name

    def get_space(self, name):
        # This function will return a space by its name
        current = self.head
        while True:
            if current.name == name:
                return current
            current = current.next_space
            if current == self.head:
                break
        return None
