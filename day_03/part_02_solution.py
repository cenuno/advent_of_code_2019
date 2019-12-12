"""
Identify the fewest combined steps the wires
must take to reach an intersection
"""
from part_01_solution import (
    positions,
    crossed_paths,
    ORIGIN
)

# remove the origin from both wires
for wire in positions:
    positions[wire].remove(ORIGIN)

# for each crossed path, sum the steps it took both wires to arrive there
steps = {"path": [], "steps": []}
for path in crossed_paths:
    steps["path"].append(path)
    steps["steps"].append(positions["wire_a"].index(path) + 1
                          + positions["wire_b"].index(path) + 1)

# find the minimum number of steps it took to reach one intersection
print(f"""
The min. number of steps to reach an intersection is {min(steps["steps"])}.
""")
