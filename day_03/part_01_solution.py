"""
To fix the circuit, you need to find the intersection
point closest to the central port. Because the wires are on a grid,
use the Manhattan distance for this measurement.
"""
from typing import List, Tuple

# create new data type
CoordPair = List[Tuple[int, int]]

# load necessary data
with open("data/day_03_input.txt", "r") as f:
    # in a list, store each wire's directional path as a list of strings
    wires = [wire.split(",") for wire in f.read().split("\n")]

# store position of central port
ORIGIN = (0, 0)


def calculate_relative_coords(direction: List[str]) -> CoordPair:
    """Determines the relative coordinate pair for each step along a wire
    Note:
        - The key term here is 'relative'. Each coordinate pair is a step in
          both the x and y direction relative to the previous step. The pairs
          are meaningless by themselves.
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


# check work
assert calculate_relative_coords(["R1004", "U518", "R309", "D991"]) == [(1004, 518), (309, -991)]
assert calculate_relative_coords(["L998", "U952", "R204", "U266"]) == [(-998, 952), (204, 266)]


def calculate_position(relative_coords: CoordPair) -> CoordPair:
    """Calculate the position of each coordinate pair from the central port
    Args:
        - relative_coords (CoordPair): the relative coordinate pair at a 
                                       particular point along a wire
    Returns:
        CoordPair: the position of each coordinate pair from the central port
    """
    output = []
    for index, coord in enumerate(relative_coords):
        if index == 0:
            # since we're assuming the origin of the central port is (0,0)
            # we can make the first position that same as the first coordinate
            output.append(coord)
        else:
            # otherwise, add the x-coord from the last coordinate
            # with the x-coord of the current coordinate;
            # the same is done for the y-coord
            position = (output[-1][0] + coord[0], output[-1][1] + coord[1])
            output.append(position)

    return output


# check work
assert calculate_position([(1004, 518), (309, -991)]) == [(1004, 518), (1313, -473)]
assert calculate_position([(-998, 952), (204, 266)]) == [(-998, 952), (-794, 1218)]
