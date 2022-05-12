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
            rand_x, rand_y = random.choice(ROWS), random.choice(COLUMNS)
            while self.board[GameBoard.covert_rows_to_nums(rand_x)][int(rand_y)-1] == "X":
                rand_x, rand_y = random.choice(ROWS), random.choice(COLUMNS)
            self.ships.append(Ship(name, hp, [rand_x, rand_y]))
            self.board[GameBoard.covert_rows_to_nums(rand_x)][int(rand_y)-1] = "X"

    def covert_rows_to_nums(row) -> int:
        rows_to_nums = {"A": 0,"B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6,"H": 7,"I": 8}
        return rows_to_nums.get(row)
        
    
    def print_board(self):
        print('  1 2 3 4 5 6 7 8 9')
        print('  -----------------')
        row_number = 0
        for row in self.board:
            row_letter = ROWS[row_number]
            print('{}|{}|'.format(row_letter, "|".join(row)))
            row_number +=1
        

class Ship(object):
    def __init__(self, name: str, hit_points: int, positions: list):
        self.name = name
        self.hit_points = hit_points
        self.positions = positions

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


    def get_position() -> list:
        row = "-"
        column = "0"

        while row not in ROWS:
            print(f"Possible rows: {ROWS}")
            row = input("Please enter the row you would like to target: ")
            if row not in ROWS:
                print("Invalid selection, Please enter a valid row")

        while column not in COLUMNS:
            print(f"Possible columns: {COLUMNS}")
            column = input("Please enter the column you would like to target: ")
            if column not in COLUMNS:
                print("Invalid selection, Please enter a valid column")

        target = [row, column]
        return target

def run_game():
    board_cpu, board_player = GameBoard(), GameBoard()
    board_player.add_ships()
    board_player.print_board()

if __name__ == "__main__":
   run_game()
    
 
