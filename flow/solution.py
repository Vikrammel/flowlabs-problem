"""
package: flow

file: solution.py

Contains functions and helper functions that determine the solution of the boarding pass problems
"""

import math
from os import path

class InvalidInputException(Exception):
    """
    InvalidInputException defines an exception encountered when an
    invalid char is read from the input seats text file.
    """

class InvalidSolutionException(Exception):
    """
    InvalidSolutionException is raised when there is an internal error in the flow
    package's solution and more than 1 missing ticket is returned.
    """

def get_seat_uid(seat: str) -> int:
    """
    get_seat_uid gets the given seat's uid defined by 8r + c
    where r is the row number (0-127) and c is the column number
    of the seat (0-7).

    A seat might be specified like FBFBBFFRLR, where F means "front",
    B means "back", L means "left", and R means "right". First 7 chars
    represent the row, last 3 represent the column.
    B, R = take upper half
    F, L = take lower half

    :returns int: uid of given seat
    :raises: InvalidInputException
    """
    row, col = 0,0 # final discovered row, col

    # iterate through seat char by char and calculate row, col
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    for index, char in enumerate(seat):
        if index < 6: # row char
            if char == 'B': # row, upper half
                row_min = math.ceil(row_min + (row_max-row_min)/2)
            elif char == 'F': # row, lower half
                row_max = math.floor(row_max - (row_max-row_min)/2)
            else:
                raise InvalidInputException
        elif index == 6: # last row char, pick upper or power
            if char == 'B': # row, upper half
                row = row_max
            elif char == 'F': # row, lower half
                row = row_min
            else:
                raise InvalidInputException
        elif index < 9: # col char
            if char == 'R': # col, upper half
                col_min = math.ceil(col_min + (col_max-col_min)/2)
            elif char == 'L': # col, lower half
                col_max = math.floor(col_max - (col_max-col_min)/2)
            else:
                raise InvalidInputException
        elif index == 9: # last col char, pick upper or lower
            if char == 'R': # col, upper half
                col = col_max
            elif char == 'L': # col, lower half
                col = col_min
            else:
                raise InvalidInputException

    return 8 * row + col

def find_solution(filename: str) -> int:
    """
    find_solution finds the largest unique seat id and missing seat id
    from the input file at ../data/<filename>

    :returns int: largest uid of all seats
    :returns int: missing ticket uid
    """
    max_uid = 0
    possible_missing_tickets = {}
    all_ticket_ids = {}

    # read input file
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "data", filename))

    with open(filepath, "r") as file_in:
        for line in file_in:
            cleaned_line = line.strip()
            seat_id = get_seat_uid(cleaned_line)
            if seat_id > max_uid:
                # new largest uid found
                max_uid = seat_id

            # add to ticket IDs
            all_ticket_ids[seat_id] = True
            # track missing ticket info
            if possible_missing_tickets.get(seat_id):
                # no longer 'missing', delete from possible_missing_tickets dict
                del possible_missing_tickets[seat_id]
            
            if all_ticket_ids.get(seat_id+1) is None and \
                all_ticket_ids.get(seat_id+2) is not None:
                # seat_id and seat_id+2 are present but not seat_id + 1,
                # mark as seat_id + 1 possible missing
                possible_missing_tickets[seat_id+1] = True
            if all_ticket_ids.get(seat_id-1) is None and \
                all_ticket_ids.get(seat_id-2) is not None:
                # seat_id and seat_id-2 are present but not seat_id - 1,
                # mark as seat_id - 1 possible missing
                possible_missing_tickets[seat_id-1] = True

    # check for soln. validity, should be only 1 entry
    if len(possible_missing_tickets) != 1:
        raise InvalidSolutionException

    return max_uid, list(possible_missing_tickets)[0]
