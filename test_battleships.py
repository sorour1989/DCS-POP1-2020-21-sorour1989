import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    s = (3, 2, True, 4, {(3,2), (3,3), (3,4), (3,5)})
    assert ship_type(s) == "battleship"
    
     
    #add at least one test for ship_type by the deadline of session 7 assignment
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    ship1,ship2 = (2,4,True,2),(5,6,True,1)
    fleet = [ship1,ship2]
    assert is_open_sea(4,2,fleet) == True
    
    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    ship1,ship2 = (2,4,True,2),(5,6,True,1)
    fleet = [ship1,ship2]
    new_ship = (1,2,False,3)
    assert ok_to_place_ship_at(is_open_sea(new_ship)) == False
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    ship1,ship2 = (2,4,True,2),(5,6,True,1)
    fleet = [ship1,ship2]
    new_ship = (7,3,True,4)
    assert place_ship_at(new_ship,fleet) == [ship1,ship2,new_ship]
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
     fleet = [(1,2,False,3,{(1,2),(2,2),(3,2)}),(3,0,False,2,{(3,0),(4,0)}),(5,3,True,2,{(5,3),(5,4)}),(8,1,True,2,{(8,1),(8,2)})]
    assert check_if_hits(5,4,fleet) == True
   
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    fleet = [(1,2,False,3,{(1,2),(2,2),(3,2)}),(3,0,False,2,{(3,0),(4,0)}),(5,3,True,2,{(5,3),(5,4)}),(8,1,True,2,{(8,1),(8,2)})]
    assert hit(3,2,fleet) == ((1,2,False,3,{(1,2),(2,2),(3,2)}),[(1,2,False,2,{(1,2),(2,2)}),(3,0,False,2,{(1,2),
                                                  (4,0)}),(5,3,True,2,{(5,3),(5,4)}),(8,1,True,2,{(8,1),(8,2)})])
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    fleet = [(1,2,False,3,{(1,2),(2,2),(3,2)}),(8,1,True,2,{(8,1),(8,2)})]
    assert are_unsunk_ships_left(fleet) == True
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
