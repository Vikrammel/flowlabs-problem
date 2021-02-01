"""
package: tests

file: flow_test.py

Tests the solution and helper functions in the 'flow' package
"""

import flow.solution as solution

def test_get_seat_uid():
    """
    test_get_seat_uid tests the cases given in question.md
    """
    assert solution.get_seat_uid("BFFFBBFRRR") == 567
    assert solution.get_seat_uid("FFFBBBFRRR") == 119
    assert solution.get_seat_uid("BBFFBBFRLL") == 820

def test_find_solution():
    """
    test_find_solution tests whether the solution to finding 
    the largest seat id and missing seat id are correct
    """
    assert solution.find_solution("input.txt") == (930, 515)
