import random

ships = {"destroyer": 2,
         "cruiser": 3,
         "submarine": 3,
         "battleship": 4,
         "carrier": 5,
         }

possible_columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
possible_rows = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')


class Player(object):

    def __init__(self, name):
        self.name = name
        self.ships = []
        self.hits = []
        self.misses = []

    def add_ship(self, ship):
        """
        "This method adds a ship object to the player object ships list"
        :param ship: ship to be added
        :return: void
        """
        self.ships.append(ship)


class Ship(object):

    def __init__(self, name, hit_points=3):
        self.name = name
        self.hit_points = hit_points
        self.alive = True
        self.positions = []

    def add_random_positions(self):
        row = random.choice(possible_rows)
        column = random.choice(possible_columns)
        #need to add condition for if positions already are taken
        self.positions.append([row.upper(), column])

    def add_positions(self):
        print(f"Please set a position for your {self.name}")
        ship_pos = get_position()
        #need to add condition for if positions already are taken
        self.positions.append(ship_pos)

    def valid_directions(self, position: list, hit_points):
        directions = ["north", "south", "east", "west"]
        for val in position:
            if val in (possible_rows[0:(hit_points-1)]):
                directions.remove("north")
            elif val in possible_rows[(-hit_points)+1::]:
                directions.remove("south")
            elif val in (possible_columns[0:(hit_points-1)]):
                directions.remove("west")
            elif val in possible_columns[(-hit_points)+1::]:
                directions.remove("east")

            return directions


def get_position() -> list:
    row = "-"
    column = "0"

    while row not in possible_rows:
        print(f"Possible rows: {possible_rows}")
        row = input("Please enter the row you would like to target: ")
        if row.upper() not in possible_rows:
            print("Invalid selection, Please enter a valid row")

    while column not in possible_columns:
        print(f"Possible columns: {possible_columns}")
        column = input("Please enter the column you would like to target: ")
        if column not in possible_columns:
            print("Invalid selection, Please enter a valid column")

    target = [row.upper(), column]
    return target


def switch_player(player: int) -> int:
    """
    The function switch which players turn it is
    :param player: the current player turn
    :return: the next player to have a turn
    """
    if player == 1:
        player = 2
    else:
        player = 1
    return player


if __name__ == "__main__":
    player_cpu = Player("cpu")
    player_1 = Player("player1")
    for ship in ships:
        ship_to_add = Ship(ship)
        player_1.add_ship(ship_to_add)

    for ship in player_1.ships:
        ship.add_positions()

    for ship in ships:
        ship_to_add = Ship(ship)
        player_cpu.add_ship(ship_to_add)
    for ship in player_cpu.ships:
        ship.add_random_positions()

for ship in player_cpu.ships:
    print(ship.positions)

