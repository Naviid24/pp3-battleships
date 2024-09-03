import random
from random import randrange


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

    def add_ship_for_player(self, ship):

        while True:
            print("Place the ship manually(m) automatically (a)?")
            print("Type 'exit' to quit:")
            choice = str(input("m or a or exit \n")).lower()
            if choice == "m":
                self.player_board.add_ship(ship)
                break
            elif choice == "a":
                self.player_board.auto_add_ship(ship)
                break
            elif choice == "exit":
                print("Exiting the game.")
                exit()
            else:
                print("Invalid data entered.please try again")

    def show_game_boards(self):
        print("\nPlayer's Board:")
        # Reveal ships on the player's board
        self.player_board.show_board(reveal_ships=True)
        print("\nComputer's Board:")
        # Hide ships on the computer's board
        self.computer_board.show_board(reveal_ships=False)

    def get_shot(self, guesses):
        while True:
            try:
                shot = input("Please enter your guess: \n")
                shot = int(shot)
                if 0 <= shot <= 99 and shot not in guesses:
                    guesses.append(shot)
                    return shot
                else:
                    print("Invalid input data entered or used number entered")
            except ValueError:
                print("Invalid input. Please enter a valid number 0-99.")

    def computer_shot(self):
        if self.computer_tactics:
            shot = self.computer_tactics.pop(0)
        else:
            shot = randrange(100)
        while shot in self.computer_guesses:
            shot = randrange(100)
        self.computer_guesses.append(shot)
        return shot

    def update_scores(self, hits, is_player):
        if hits:
            if is_player:
                self.player_score += 1
            else:
                self.computer_score += 1

    def play_turn(self, is_player):
        if is_player:

            # Player's turn
            shot = self.get_shot(self.player_guesses)
            hits = self.computer_board.check_shot(shot)
            self.update_scores(hits, is_player)
            self.computer_board.show_board(reveal_ships=False)
        else:
            # Computer's turn
            shot = self.computer_shot()
            hits = self.player_board.check_shot(shot)
            self.update_scores(hits, is_player)
            self.player_board.show_board(reveal_ships=True)
            print(f"Player Score: {self.player_score}")
            print(f"Computer Score: {self.computer_score}")
            print("-"*35)
            if hits:
                self.computer_tactics = self.calc_tactics(shot)
            elif self.computer_tactics:
                self.computer_tactics.pop(0)

    def calc_tactics(self, shot):
        tactics = [shot - 1, shot + 1, shot - 10, shot + 10]
        valid_tactics = [
             t for t in tactics
             if 0 <= t < 100 and t not in self.computer_guesses
        ]
        random.shuffle(valid_tactics)
        return valid_tactics

    def check_win(self, board):
        return all(ship.is_sunk() for ship in board.ships)

    def ask_play_again(self):
        while True:
            choice = input("Do you want to play again? (y/n): \n").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                print("Thank you for playing!")
                return False
            else:
                print("Invalid data, please enter 'y' for yes or 'n' for no.")

    def start(self):
        while True:
            self.__init__()  # Reset the game state
            self.setup()
            for i in range(80):
                self.play_turn(is_player=True)
                if self.check_win(self.computer_board):
                    print(f"End of game - Player wins in {i} turns!")
                    break
                self.play_turn(is_player=False)
                if self.check_win(self.player_board):
                    print(f"End of game - Computer wins in {i} turns!")
                    break
            if not self.ask_play_again():
                break


def welcome_in():
    """
    Welcome to the user and explain about the game and the game's rules.
    Ask user to enter his name.
    """
    print("-" * 35)
    print("Welcome Captain to THE BATTLE OF SHIPS!!")
    print("Number of ships: 6 in vary length")
    print("The board size is 10 x 10")
    print("You can locate your ship horizentaly or verticaly")
    print("Your ship should be located in one row or column")
    print("Top left coordinate is 0")
    print("Bottom right coordinate is 99")
    print("You can not guess same number more than once")
    print(
        "To locate your ship vertically, add or subtract 10 "
        "to your first number and the last number you chose"
    )
    print(
        "To locate your ship horizontally, add or subtract 1 "
        "from the first and last number you chose"
    )
    print("To start the game please enter your name below")
    print("-" * 35)
    while True:
        name = input("Please enter your name: \n")
        if not name.isalpha():
            print("Invalid data entered, please enter your name")
        else:
            print(f"welcome Captain {name} ")
            break
    print("-" * 35)


# To start the game
welcome_in()
game = Game()
game.start()
