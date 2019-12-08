"""
Identify the fewest combined steps the wires
must take to reach an intersection
"""
from part_01_solution import (
    positions,
    crossed_paths
)

print(positions["wire_a"][0:10])
print(crossed_paths[0:10])
print(positions["wire_a"].index(crossed_paths[0]))