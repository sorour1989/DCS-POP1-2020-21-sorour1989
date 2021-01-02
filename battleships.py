#see the readme.md file for description and data 

#def right_shot(ship):
    #if ship[0]is.integer()
#--------------

# defining classes
# define classes first, then test all of the methods for another time
# class Ship:
#     type = "UNDEFINED"
#     length = 0
#     _hit = 0     # _ means attribute is private
#     hit_coords = list()
#---------------
# import random
# import numpy as np
#
#
# def ship():
#
#     row = random.randint(0,9)
#     column = random.randint(0,9)
#     horizontal = random.choice([True,False])
#     length = random.randint(1,4)
#     ships = tuple(np.array([row, column, horizontal, length]))
#
#     return ships
#
# f= ship()
# print(f)
#
#
#
#
#
#
#
#
#
#
#
# def fleet
#
#
#
# def is_sunk(ship):
#     if len(ship[4]) == ship[3]:
#         return 'True'
#     else:
#         return 'False'
#
#
# #def squares_occupied(ship):
#
#
#
#
# def ship_type(ship):
#     length = [1, 2, 3, 4]
#     if ship[3] not in length:
#         return "wrong length"
#     else:
#         if ship[3] == length[0]:
#             return "Submarine"
#         elif ship[3] == length[1]:
#             return "Destroyer"
#         elif ship[3] == length[2]:
#             return "Cruiser"
#         else:
#             return "Battleship"
#
#
# def is_open_sea(row, column, fleet):
#     for ship in fleet:
#         rows_squares = [ship[0]]
#         column_squares = [ship[1]]
#         if ship[2] == 'True':
#             for i in range(ship[3]-1):
#                 ship[1] += 1
#                 column_squares.append(ship[1])
#         else:
#             for i in range(ship[3]-1):
#                 ship[0] += 1
#                 rows_squares.append(ship[0])
#     if row in rows_squares or column in column_squares:
#         return 'False'
#     else:
#         return 'True'
#


from numpy import zeros
from random import choice, randint, shuffle
# from functools import lru_cache


SHIP_TYPES = {
    1: "SUBMARINE",
    2: "DESTROYER",
    3: "CRUISER",
    4: "BATTLESHIP"
}

ROW = 0
COLUMN = 1
HORIZONTAL = 2
LENGTH = 3
HITS = 4

FLEET_TYPES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def get_type(ship):
    length = ship[LENGTH]
    return SHIP_TYPES.get(length, "WRONG LENGTH")


def get_sea_map(fleet):
    # @lru_cache(1024)
    def func(*flt):
        sea = zeros([10, 10], dtype=bool)

        for row, col, horizontal, length, _ in flt:
            if horizontal:
                sea[row, col:col + length] = True
                continue

            sea[row: row + length, col] = True

        return sea
    return func(*fleet)


def is_open_sea(row: int, col: int, fleet) -> bool:
    sea = get_sea_map(fleet)

    prev_row = max(row - 1, 0)
    next_row = min(row + 2, sea.shape[0])

    prev_col = max(col - 1, 0)
    next_col = min(col + 2, sea.shape[1])

    matrix = sea[prev_row: next_row, prev_col: next_col]

    for row in matrix:
        if any(row):
            return False

    return True





def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass


def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass


def randomly_place_all_ships():
    #remove pass and add your implementation
    pass


def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
