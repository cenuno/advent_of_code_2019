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


def calculate_positions(relative_coords: CoordPair) -> CoordPair:
    """Calculate the positions for each coordinate pair from the central port
    Args:
        - relative_coords (CoordPair): the relative coordinate pair at a
                                       particular point along a wire
    Returns:
        CoordPair: the positions from each coordinate pair from the central port
    """
    output = [ORIGIN]
    for coord in relative_coords:
        # for each coordinate pair, find its intermediate positions
        for idx, val in enumerate(coord):
            # if val is a pos, take a step in the pos direction
            if val >= 0:
                step = 1
            else:
                # otherwise take a step in the neg direction
                step = -1
            for _ in range(abs(val)):
                # for each integer between 0 and the value,
                # calculate the intermediate steps between the last position
                # and the next by moving one step in the appropriate direction
                if idx == 0:
                    x_pos = (output[-1][0] + step, output[-1][1])
                    output.append(x_pos)
                else:
                    y_pos = (output[-1][0], output[-1][1] + step)
                    output.append(y_pos)
    return output


# check work
assert calculate_positions([(1, -2)]) == [(0, 0), (1, 0), (1, -1), (1, -2)]
assert calculate_positions([(2, 3), (-1, -2)]) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1, 2), (1, 1)]


def distance(point_a: Tuple[int, int],
             point_b: Tuple[int, int],
             m: int) -> float:
    """Generalized distance between two points
    Note:
        See more info here: https://xlinux.nist.gov/dads/HTML/lmdistance.html
    Args:
        - point_a (Tuple[int, int]): a coordinate pair
        - point_b (Tuple[int, int]): a coordinate pair
        - m (int): the type of distance to calculate between the points
                        Can only take three values:
                        1 -> manhattan
                        2 -> euclidean
                        More than 2 -> minkowski
    Result:
        float: the distance between the two points
    """
    abs_diff_x_exp_m = abs(point_a[0] - point_b[0]) ** m
    abs_diff_y_exp_m = abs(point_a[1] - point_b[1]) ** m
    sum_dif = abs_diff_x_exp_m + abs_diff_y_exp_m
    distance = sum_dif ** (1 / m)
    return distance


# check work
assert distance((2, 7), (14, -6), m=1) == 25.0
assert distance((2, 7), (14, -6), m=2) == 17.69180601295413
assert distance((2, 7), (14, -6), m=3) == 15.77417133438064

# calculate the relative position of each wire
relative_positions = {"wire_a": calculate_relative_coords(wires[0]),
                      "wire_b": calculate_relative_coords(wires[1])}

# calculate the position of each wire
positions = {"wire_a": calculate_positions(relative_positions["wire_a"]),
             "wire_b": calculate_positions(relative_positions["wire_b"])}

# identify the positions that are intersect
crossed_paths = list(set(positions["wire_a"]).intersection(positions["wire_b"]))
# remove the origin
crossed_paths.remove(ORIGIN)

# identify distance from each point of intersection to the central port
distances = []
for path in crossed_paths:
    distances.append(distance(ORIGIN, path, m=1))

print(f"""
There were {len(crossed_paths)} times the paths of the wires crossed.
The min. distance from one and the point of origin was {round(min(distances))}.
""")
