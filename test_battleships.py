import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    if len(s) > 4 or len(s) < 1:
        assert ship_type(s) == "Wrong Input"
    elif len(s) == 1:
        assert ship_type(s) == "Submarine"
    elif len(s) == 2:
        assert ship_type(s) == "Destroyer"
    elif len(s) == 3:
        assert ship_type(s) == "Cruisers"
    else:
        assert ship_tyoe(s) == "Battleship"
     
    #add at least one test for ship_type by the deadline of session 7 assignment
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
