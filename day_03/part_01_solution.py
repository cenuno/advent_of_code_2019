"""
To fix the circuit, you need to find the intersection
point closest to the central port. Because the wires are on a grid,
use the Manhattan distance for this measurement.
"""
from typing import List, Tuple

# load necessary data
with open("data/day_03_input.txt", "r") as f:
    # in a list, store each wire's directional path as a list of strings
    wires = [wire.split(",") for wire in f.read().split("\n")]

# store position of central port
CENTRAL_PORT_POS = (0, 0)


def calculate_sign(direction: List[str]) -> List[Tuple[int, int]]:
    """Determines the sign for each step recorded along the wire's direction
    Args:
        - direction (List[str]): the direction recorded at a particular point
                                 along a wire
    Results:
        List[Tuple[int, int]]: List of each coordinate pair, stored as a tuple
    """
    # if 'R' or 'U' appears in the direction, ensure it is a pos int;
    # otherwise make it negative
    steps = [int(dir[1:])
             if dir.find("R") == 0 or dir.find("U") == 0
             else -int(dir[1:])
             for dir in direction]

    # store each odd numbered element as the x-coordinate
    x_coords = steps[0::2]
    # store each even numbered element as the y-coordinate
    y_coords = steps[1::2]

    if len(y_coords) == len(x_coords):
        pass
    elif len(y_coords) > len(x_coords):
        # if there are more y-coords than x-coords
        # pad the difference in x_coords with zeros
        diff = len(y_coords) - len(x_coords)
        x_coords.extend([0] * diff)
    else:
        # if there are more x-coords than y-coords
        # pad the difference in y_coords with zeros
        diff = len(x_coords) - len(y_coords)
        y_coords.extend([0] * diff)

    # create the coordinate pairs
    coords = []
    for x_coord, y_coord in zip(x_coords, y_coords):
        coords.append((x_coord, y_coord))

    return coords


assert calculate_sign(["R1004", "U518", "R309", "D991"]) == [(1004, 518), (309, -991)]
