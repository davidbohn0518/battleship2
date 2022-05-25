import random


ships = {"destroyer": 2,
         "cruiser": 3,
         "submarine": 3,
         "battleship": 4,
         "carrier": 5,
         }

COLUMNS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


class GameBoard(object):

    def __init__(self):
        self.board = []
        self.create_board()
        self.guesses = []
        self.ships = []
    
    def create_board(self):
        for row in range(len(ROWS)):
            self.board.append([])
            for col in range(len(COLUMNS)):
                self.board[row].append(' ')

    def add_ships(self):
        """Get a random position.
        Check to see is random position on self.board == 'X'
        Then instantiate a ship object and set self.board to of random postion to 'X'"""
        for name, hp in ships.items():
            rand_x, rand_y = get_random_location()
            while self.board[covert_rows_to_nums(rand_x)][int(rand_y)-1] == "X":
                rand_x, rand_y = get_random_location()
            self.ships.append(Ship(name, hp, [rand_x, rand_y]))
            self.board[covert_rows_to_nums(rand_x)][int(rand_y)-1] = "X"
     
    def print_board(self):
        print('  1 2 3 4 5 6 7 8 9')
        print('  -----------------')
        row_number = 0
        for row in self.board:
            row_letter = ROWS[row_number]
            print('{}|{}|'.format(row_letter, "|".join(row)))
            row_number +=1

    def ship_lookup(self, position):
        for s in self.ships:
            if s.positions == position:
                return s

    def alive_check(self):
        counter = 0
        for ship in self.ships:
            if counter == len(self.ships):
                return False
            if ship.alive == False:
                counter += 1
            else:
                return True


class Ship(object):
    def __init__(self, name: str, hit_points: int, positions: list):
        self.name = name
        self.hit_points = hit_points
        self.positions = positions
        self.alive = True

    def valid_directions(self, position: list, hit_points):
        directions = ["north", "south", "east", "west"]
        for val in position:
            if val in (ROWS[0:(hit_points-1)]):
                directions.remove("north")
            elif val in ROWS[(-hit_points)+1::]:
                directions.remove("south")
            elif val in (COLUMNS[0:(hit_points-1)]):
                directions.remove("west")
            elif val in COLUMNS[(-hit_points)+1::]:
                directions.remove("east")

            return directions

def fire_shot(tboard: GameBoard, gboard: GameBoard):
    target = get_location()
    
    while gboard.board[covert_rows_to_nums(target[0])][int(target[1])-1] != " ":
        print("You have already guessed this location. Please Try Again")
        target = get_location()
    if tboard.board[covert_rows_to_nums(target[0])][int(target[1])-1] == "X":
        ship = tboard.ship_lookup(target)
        print("You sank the opponents {}".format(ship.name))
        gboard.board[covert_rows_to_nums(target[0])][int(target[1])-1] = "X"
        ship.alive = False
    else:
        print("You missed!")
        gboard.board[covert_rows_to_nums(target[0])][int(target[1])-1] = "O"
        gboard.guesses.append(target)

def cpu_ai(board: GameBoard):
    target = get_random_location()

    while board.board[covert_rows_to_nums(target[0])][int(target[1])-1] != " " and board.board[covert_rows_to_nums(target[0])][int(target[1])-1] != "X":
        target = get_random_location()
    if board.board[covert_rows_to_nums(target[0])][int(target[1])-1] == "X":
        ship = board.ship_lookup(target)
        print("Your oppenant sank your {}".format(ship.name))
        board.board[covert_rows_to_nums(target[0])][int(target[1])-1] = "^"
        ship.alive = False
    else:
        board.board[covert_rows_to_nums(target[0])][int(target[1])-1] = "O"
        board.guesses.append(target)
        print("Your opponent missed!")
            
def covert_rows_to_nums(row) -> int:
    rows_to_nums = {"A": 0,"B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6,"H": 7,"I": 8}
    return rows_to_nums.get(row)

def get_random_location():
    rand_x, rand_y = random.choice(ROWS), random.choice(COLUMNS)
    return [rand_x, rand_y]

def get_location():
    row = "-"
    col = "0"

    while row not in ROWS:
        print(f"Possible rows: {ROWS}")
        row = input("Please enter the row you would like to target: ")
        if row not in ROWS:
            print("Invalid selection, Please enter a valid row")

    while col not in COLUMNS:
        print(f"Possible columns: {COLUMNS}")
        col = input("Please enter the column you would like to target: ")
        if col not in COLUMNS:
            print("Invalid selection, Please enter a valid column")

    return [row, col]
               
        

def run_game():
    board_cpu, board_pguess, board_player = GameBoard(), GameBoard(), GameBoard()
    board_player.add_ships()
    board_cpu.add_ships()
    
    while board_player.alive_check() and board_cpu.alive_check():
        board_pguess.print_board()
        board_player.print_board()
        fire_shot(board_cpu, board_pguess)
        cpu_ai(board_player)

    if board_player.alive_check():
        print("Well Done! You WIN!!!!")
    else:
        print("What's the matter?!? The computer too good for you? TRY AGAIN!!!")
    
    
if __name__ == "__main__":
   run_game()
    
 
