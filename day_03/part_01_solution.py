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
    """Determines the sign for each direction recorded along the wire
    Args:
        - direction (List[str]): the direction recorded at a particular point
                                 along a wire
    Results:
        List[Tuple[int, int]]: List of each coordinate pair, stored as a tuple
    """
    pass
