class BoardSpace:
    def __init__(self, name, space_type, details=None):
        self.name = name
        self.space_type = space_type
        self.details = details if details else {}
        self.next_space = None