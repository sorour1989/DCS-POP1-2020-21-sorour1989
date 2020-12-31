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
import random
import numpy as np


def ship():

    row = random.randint(0,9)
    column = random.randint(0,9)
    horizontal = random.choice([True,False])
    length = random.randint(1,4)
    ships = tuple(np.array([row, column, horizontal, length]))

    return ships

f= ship()
print(f)











def fleet



def is_sunk(ship):
    if len(ship[4]) == ship[3]:
        return 'True'
    else:
        return 'False'


#def squares_occupied(ship):




def ship_type(ship):
    length = [1, 2, 3, 4]
    if ship[3] not in length:
        return "wrong length"
    else:
        if ship[3] == length[0]:
            return "Submarine"
        elif ship[3] == length[1]:
            return "Destroyer"
        elif ship[3] == length[2]:
            return "Cruiser"
        else:
            return "Battleship"


def is_open_sea(row, column, fleet):
    for ship in fleet:
        rows_squares = [ship[0]]
        column_squares = [ship[1]]
        if ship[2] == 'True':
            for i in range(ship[3]-1):
                ship[1] += 1
                column_squares.append(ship[1])
        else:
            for i in range(ship[3]-1):
                ship[0] += 1
                rows_squares.append(ship[0])
    if row in rows_squares or column in column_squares:
        return 'False'
    else:
        return 'True'





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
