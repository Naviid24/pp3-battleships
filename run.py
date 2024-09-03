

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


class Board:
    """
    Main board class. Has methods for adding ships,
    guesses, and printing the board.
    """
    def __init__(self):
        self.taken_positions = []
        self.ships = []
        self.hits = []
        self.misses = []
        self.completions = []

    def check_ok(self, boat):
        boat.sort()
        for i in range(len(boat)):
            num = boat[i]
            if num in self.taken_positions:
                return False

            elif num < 0 or num > 99:
                return False
            elif num % 10 == 9 and i < len(boat)-1:
                if boat[i+1] % 10 == 0:
                    return False
            if i != 0:
                if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                    return False
        return True

    def add_ship(self, ship):

        while True:
            boat = []
            print(f"Enter your ship of length {ship.size}")
            for _ in range(ship.size):
                while True:
                    try:
                        boat_num = input("Please enter a number: ")
                        boat_num = int(boat_num)
                        # Check if the number is within the valid range
                        if not (0 <= boat_num <= 99):
                            raise ValueError("Enter a number between 0-99.")
                        boat.append(boat_num)
                        break   # Exit the inner loop if the input is valid
                    except ValueError as e:
                        print(f"Error: {e}. Please enter a valid number.")

        # Check if the coordinates are valid
        if self.check_ok(boat):
            print("Your ship is located truely")
            print()
            ship.positions = boat
            self.taken_positions += boat
            self.ships.append(ship)
            break
        else:
            print("Error: Please enter valid number")

    def auto_add_ship(self, ship):
        while True:
            start = randrange(99)
            direction = randrange(1, 5)
            boat = []

            if direction == 1:
                boat = [start - i*10 for i in range(ship.size)]
            elif direction == 2:
                boat = [start + i for i in range(ship.size)]
            elif direction == 3:
                boat = [start + i*10 for i in range(ship.size)]
            elif direction == 4:
                boat = [start - i for i in range(ship.size)]

            if self.check_ok(boat):
                ship.positions = boat
                self.taken_positions += boat
                self.ships.append(ship)
                break                      