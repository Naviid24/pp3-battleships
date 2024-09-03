

class Ship:
    """
    The main ship object returns the size of the ship
    and any ships that have been sunk.
    """
    def __init__(self, size):
        self.size = size
        self.positions = []

    def is_sunk(self):
        return len(self.positions) == 0