from shipping.battleships import *
import pytest


@pytest.mark.parametrize("num1, result",
                         [
                             ((2, 3, False, 2, 2), True),
                             ((6, 1, True, 4, 3), False),
                             ((5, 9, False, 3, 3), True),
                             ((0, 9, True, 4, 2), False),
                             (("1", 7, True, 3, 1), False)
                         ])
def test_is_sunk(num1, result):

    assert is_sunk(num1) is result





@pytest.mark.parametrize("ship, result",
                         [
                             ((2, 3, False, 2, 2), "DESTROYER"),
                             ((6, 1, True, 4, 3), "BATTLESHIP"),
                             ((5, 9, False, 3, 3), "CRUISER"),
                             ((0, 9, True, 5, 2), "WRONG LENGTH"),
                             ((1, 7, True, 1, 1), "SUBMARINE")
                         ])
def test_ship_type1(ship, result):
    assert ship_type(ship) == result


@pytest.mark.parametrize("row, col, fleet, result",
                         [
                            (2, 4, [(2, 4, True, 2, 0), (5, 6, True, 1, 0)], False),
                            (6, 7, [(6, 1, False, 3, 0), (9, 3, True, 2, 0), (5, 4, True, 4, 0)], False),
                            (1, 0, [(5, 7, False, 1, 0), (8, 0, True, 3, 0), (2, 0, True, 2, 0)], False),
                            (0, 9, [(7, 1, False, 3, 0)], True),
                            (5, 5, [(0, 9, False, 1, 0), (2, 0, False, 3, 0), (5, 9, False, 3, 0),
                                    (7, 0, True, 4, 0)], True)
                         ]
                         )
def test_is_open_sea(row, col, fleet, result):
    assert is_open_sea(row, col, fleet) is result



@pytest.mark.parametrize("row, col, horizontal, length, fleet, result",
                         [
                            (2, 4, True, 2, [(2, 4, True, 2, 0), (5, 6, True, 1, 0)], False),
                            (1, 2, False, 1, [(6, 1, False, 3, 0), (9, 3, True, 2, 0), (5, 4, True, 4, 0)], True),
                            (3, 5, True, 2, [(5, 7, False, 1, 0), (8, 0, True, 3, 0), (2, 0, True, 2, 0)], True),
                            (8, 3, True, 2, [(7, 1, False, 3, 0)], True),
                            (5, 5, True, 4, [(0, 9, False, 1, 0), (2, 0, False, 3, 0), (5, 9, False, 3, 0),
                             (7, 0, True, 4, 0)], False)
                         ]
                         )
def test_ok_to_place_ship_at(row, col, horizontal, length, fleet, result):
    assert ok_to_place_ship_at(row, col, horizontal, length, fleet) is result


@pytest.mark.parametrize("row, col, horizontal, length, fleet, result",
                         [
                            (1, 4, True, 2, [(2, 4, True, 2, 0), (5, 6, True, 1, 0)], "Conflict detected."),
                (3, 4, False, 2, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0)], "Conflict detected.")

                         ]
                         )
def test_place_ship_at(row, col, horizontal, length, fleet, result):
    with pytest.raises(RuntimeError):
        assert place_ship_at(row, col, horizontal, length, fleet) == result


@pytest.mark.parametrize("row, col, horizontal, length, fleet, result",
                         [
                             (6, 0, False, 3, [(2, 4, True, 2, 0), (5, 6, True, 1, 0)], [(2, 4, True, 2, 0),
                              (5, 6, True, 1, 0), (6, 0, False, 3, 0)]),
                             (3, 0, False, 2, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0)],
                              [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0)]),
                             (7, 2, True, 4, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0)],
                              [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0),
                               (7, 2, True, 4, 0)])
                         ]
                         )
def test_place_ship_at_1(row, col, horizontal, length, fleet, result):

    assert place_ship_at(row, col, horizontal, length, fleet) == result


@pytest.mark.parametrize("row, col, fleet, result",
                         [
                             (6, 0, [(2, 4, True, 2, 0), (5, 6, True, 1, 0)], False),
                             (7, 0, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0)], True),
                             (8, 4, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0)],
                              False),
                             (4, 0, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0),
                                     (7, 3, True, 4, 0)], True),
                             (9, 4, [(2, 4, True, 2, 0), (5, 6, True, 1, 0), (6, 0, False, 3, 0), (3, 0, False, 2, 0),
                                     (2, 9, False, 3, 0)], False)
                         ]
                         )
def test_check_if_hits(row, col, fleet, result):
    assert check_if_hits(row, col, fleet) == result
---------------
def test_hit1():
    fleet = [
        (1, 2, False, 3, {(1, 2), (2, 2), (3, 2)}),
        (3, 0, False, 2, {(3, 0), (4, 0)}),
             (5, 3, True, 2, {(5, 3), (5, 4)}), (8, 1, True, 2, {(8, 1), (8, 2)})]
    assert hit(3, 2, fleet) == (
        (1, 2, False, 3, {(1, 2), (2, 2), (3, 2)}), [(1, 2, False, 2, {(1, 2), (2, 2)}), (3, 0, False, 2, {(1, 2),
                                                                                                           (4, 0)}),
                                                     (5, 3, True, 2, {(5, 3), (5, 4)}),
                                                     (8, 1, True, 2, {(8, 1), (8, 2)})])
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline


def test_are_unsunk_ships_left1():
    fleet = [(1, 2, False, 3, {(1, 2), (2, 2), (3, 2)}), (8, 1, True, 2, {(8, 1), (8, 2)})]
    assert are_unsunk_ships_left(fleet) is True
    # add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
