from numpy import zeros
from random import choice, randint, shuffle
from functools import lru_cache
from typing import Tuple, List, Union


ShipType = Tuple[int, int, bool, int, int]
FleetType = List[ShipType]

SHIP_TYPES = {
    1: "SUBMARINE",
    2: "DESTROYER",
    3: "CRUISER",
    4: "BATTLESHIP"
}


class Ship:
    row: int = 0
    column: int = 1
    horizontal: int = 2
    length: int = 3
    hits: int = 4


FLEET_TYPES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def ship_type(ship):
    length = ship[Ship.length]
    return SHIP_TYPES.get(length, "WRONG LENGTH")


def get_sea_map(fleet: FleetType):

    @lru_cache(128)
    def func(*flt):
        sea = zeros([10, 10], dtype=bool)

        for row, col, horizontal, length, _ in flt:
            if horizontal:
                sea[row, col:col + length] = True
                continue

            sea[row: row + length, col] = True

        return sea
    return func(*fleet)


def is_open_sea(row: int, col: int, fleet: FleetType) -> bool:
    sea = get_sea_map(fleet)

    prev_row = max(row - 1, 0)
    next_row = min(row + 2, sea.shape[0])

    prev_col = max(col - 1, 0)
    next_col = min(col + 2, sea.shape[1])

    matrix = sea[prev_row: next_row, prev_col: next_col]

    return all(not any(row) for row in matrix)


def ok_to_place_ship_at(row: int, column: int, horizontal: bool, length: int, fleet: FleetType) -> bool:
    sea = get_sea_map(fleet)

    if horizontal and column + length > sea.shape[1]:
        return False

    if not horizontal and row + length > sea.shape[0]:
        return False

    for offset in range(length):
        if horizontal:
            s_row = row
            s_col = column + offset
        else:
            s_row = row + offset
            s_col = column

        if not is_open_sea(s_row, s_col, fleet):
            return False

    return True


def place_ship_at(row: int, column: int, horizontal: bool, length: int, fleet: FleetType) -> FleetType:
    if not ok_to_place_ship_at(row, column, horizontal, length, fleet):
        raise RuntimeError("Conflict detected.")

    return fleet + [(row, column, horizontal, length, 0)]


def check_if_hits(row: int, column: int, fleet) -> bool:
    return find_index_of_ship_at(row, column, *fleet) is not None


@lru_cache(128)
def find_index_of_ship_at(row: int, column: int, *fleet) -> Union[int, None]:
    for index, (x1, y1, horizontal, length, _) in enumerate(fleet):
        if not horizontal:
            x2, y2 = x1 + length, y1
        else:
            x2, y2 = x1, y1 + length

        if row < x1 or row > x2 or column < y1 or column > y2:
            continue

        dxc = row - x1
        dyc = column - y1

        dxl = x2 - x1
        dyl = y2 - y1

        cross = dxc * dyl - dyc * dxl

        if cross == 0:
            return index

    return None


def hitted(row: int, column: int, fleet: FleetType) -> FleetType:
    ship_index = find_index_of_ship_at(row, column, *fleet)

    ship = list(fleet[ship_index])

    if ship[Ship.hits] < ship[Ship.length]:
        ship[Ship.hits] += 1

    fleet[ship_index] = tuple(ship)

    return fleet


def hit(row: int, column: int, fleet: FleetType):
    ship_index = find_index_of_ship_at(row, column, *fleet)

    ship = list(fleet[ship_index])

    if ship[Ship.hits] < ship[Ship.length]:
        ship[Ship.hits] += 1

    fleet[ship_index] = tuple(ship)

    return fleet, tuple(ship)


def is_sunk(ship: ShipType):
    return ship[Ship.hits] == ship[Ship.length]


def are_unsunk_ships_left(fleet: FleetType):
    return not all(map(is_sunk, fleet))



def randomly_place_all_ship(fleet: FleetType):
    initial_fleet = fleet.copy()
    counter = 0
    shuffle(FLEET_TYPES)
    n_ship = 0

    while n_ship < 10:
        row = randint(0, 9)
        col = randint(0, 9)
        direction = choice([True, False])
        s_type = FLEET_TYPES[n_ship]
        ship: ShipType = (row, col, direction, s_type, 0)
        counter += 1
        try:
            fleet = place_ship_at(*ship[:-1], fleet=fleet)
            n_ship += 1
        except RuntimeError:
            pass

        if counter > 1 and counter % 500 == 0:
            fleet = initial_fleet
            n_ship = 0

    return fleet


def main():
    fleet_data = list()
    fleet_data = randomly_place_all_ship(fleet_data)
    n_shots = 0
    sunken_ship, misses, hits = set(), set(), set()
    shoots = []


    print("Enter coordinates 0 to 9 separated by comma or press Q to exit.")
    print("Example: ROW,COLUMN")

    while True:

        command = input(f"[SHOTS: {n_shots:<3}] >>> coordinates: ")

        if command == "Q":
            break

        n_shots += 1

        if n_shots > 100:
            print("You exceeded the legal number of shots.\nGame Over")
            break

        try:
            row, column = map(int, map(str.strip, command.split(",")))
        except ValueError:
            print("Invalid input")
            continue

        if check_if_hits(row, column, fleet_data) and not [row, column] in shoots:
            fleet_data = hitted(row, column, fleet_data)
            hits.add((row, column))
            shoots.append([row, column])
            print("It was a hit.")
        else:
            misses.add((row, column))
            print("You missed it.")
            continue

        for ship in set(fleet_data) - sunken_ship:
            if is_sunk(ship):
                print(f"You have sunken a '{ship_type(ship)}'.")

            sunken_ship.add(ship)

        if not are_unsunk_ships_left(fleet_data):
            print(f"You've sunk 'em all in {n_shots} shots")
            break

    print("Bye")


if __name__ == "__main__":
    main()
