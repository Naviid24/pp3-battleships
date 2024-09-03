

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

    def show_board(self, reveal_ships=False):
        print("            Battleships    ")
        print("    0  1  2  3  4  5  6  7  8  9")
        place = 0
        for x in range(10):
            row = ""
            for y in range(10):
                if (
                    reveal_ships and place in self.taken_positions and
                    place not in self.hits and place not in self.completions
                ):
                    ch = " @ "  # Display ship positions if revealing ships
                elif place in self.hits:
                    ch = " X "
                elif place in self.misses:
                    ch = " o "
                elif place in self.completions:
                    ch = " S "
                else:
                    ch = " _ "
                row += ch
                place += 1
            print(f"{x}  {row}")
        print("-"*35)

    def check_shot(self, shot):
        for ship in self.ships:
            if shot in ship.positions:
                ship.positions.remove(shot)
                if ship.is_sunk():
                    self.completions.append(shot)
                else:
                    self.hits.append(shot)
                return True
        self.misses.append(shot)
        return False

class Game:
    """
    The Game class manages the setup and progression of the game.
    It includes methods to initialize the game, handle shots on
    both the player's and computer's boards, and track the scores
    for both. At the end of the game, it determines the winner
    and allows the user to either play again or quit.
    """
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()
        self.player_guesses = []
        self.computer_guesses = []
        self.computer_tactics = []
        self.player_score = 0
        self.computer_score = 0

    def setup(self):
        ships_sizes = [5, 4, 3, 3, 2, 2]
        # Automatically place ships on the computer's board
        for size in ships_sizes:
            ship = Ship(size)
            self.computer_board.auto_add_ship(ship)

        # Allow the player to choose manual or automatic
        # placement for each ship
        for size in ships_sizes:
            ship = Ship(size)
            # Use the new method for placing ships
            self.add_ship_for_player(ship)
        print("-" * 35)
        self.show_game_boards()
