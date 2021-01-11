from typing import List, Set, Tuple, Callable, NoReturn
from shipping.battleships import (
    get_sea_map, find_index_of_ship_at, ship_type,
    is_sunk, randomly_place_all_ship, check_if_hits,
    are_unsunk_ships_left, hitted, Ship, FleetType
)


RowColumn = Tuple[int, int]


def get_column_names(row: List[bool]) -> str:
    result = "  "
    for col_ind, _ in enumerate(row):
        result += f"{col_ind:^3}"
    result += "\n"

    return result


def get_column_symbol(hits: Set[RowColumn], misses: Set[RowColumn], fleet: FleetType) -> Callable[[int, int], str]:
    def get_symbol(row: int, col: int) -> str:
        if (row, col) in hits:
            s_ind = find_index_of_ship_at(row, col, *fleet)
            ship = fleet[s_ind]
            s_type = ship_type(ship)

            if is_sunk(ship):
                return f" {s_type[0]} "
            elif 0 < ship[Ship.hits] < ship[Ship.length]:
                return " * "

        if (row, col) in misses:
            return " - "
        else:
            return " ~ "

    return get_symbol


def visualise(fleet: FleetType, hits: Set[RowColumn], misses: Set[RowColumn]) -> str:
    result = str()
    sea = get_sea_map(fleet)
    column_symbol = get_column_symbol(hits, misses, fleet)

    for row_ind, row in enumerate(sea):
        if row_ind == 0:
            result += get_column_names(row)

        result += f"{row_ind:<2}"

        columns = [
            column_symbol(row_ind, col_ind)
            for col_ind, _ in enumerate(row)
        ]

        result += str.join("", columns) + "\n"

    return result


def main() -> NoReturn:
    fleet_data = list()
    fleet_data = randomly_place_all_ship(fleet_data)
    n_shots = 0
    sunken_ship, misses, hits = set(), set(), set()
    shoots = []

    print("Enter coordinates 0-9 separated by comma or press Q to exit.")
    print("Example: ROW,COLUMN")
    print("=~" * 20, end="\n\n")

    while True:

        visual = visualise(fleet_data, hits, misses)
        print(visual)
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
            visual = visualise(fleet_data, hits, misses)
            print(f"You've sunk them all in {n_shots} shots")
            print(visual)
            break

    print("Bye")


if __name__ == "__main__":
    main()
