"""
Restore the gravity assist program (your puzzle input) to the
"1202 program alarm" state it had just before the last computer caught fire.
"""
from typing import List

# store a new data type
Vector = List[int]


def calculate_intcode_program(data: Vector) -> Vector:
    """Conducts optcode logic on the Intcode program
    Args:
        - data (Vector): an Intcode program

    Returns:
        Vector: the results of the Intcode program following the opcode logic
    """
    # store the counter
    counter = 0
    # store steps to move
    steps = 4
    # store how many sequences to run
    # note: sequences need to be whole numbers so we're rounding up
    sequences = range(0, round(len(data) / 4))
    # store a copy of the data
    ints = data.copy()

    for seq in sequences:
        if ints[counter] == 1:
            # if the optcode int is 1
            # sum the values of the two positions next to ints[counter]
            # and place its value in the position 3 steps ahead of ints[counter]
            sum_of_next_two = ints[ints[counter + 1]] + ints[ints[counter + 2]]
            ints[ints[counter + 3]] = sum_of_next_two
        elif ints[counter] == 2:
            # if the optcode int is 2
            # multiple the values of the two positions next to ints[counter]
            # and place its value in the position 3 steps ahead of ints[counter]
            prod_of_next_two = ints[ints[counter + 1]] * ints[ints[counter + 2]]
            ints[ints[counter + 3]] = prod_of_next_two
        elif ints[counter] == 99:
            # if the optcode is 99
            # halt the program entirely
            break
        else:
            # if the optcode is anything other than 1, 2, or 99
            # halt the program with an error message
            print(f"""
            A non-optcode integer was found at index {counter}: {ints[counter]}
            """)
            break

        # move the counter forward
        counter += steps

    return ints


# load necessary data
with open("data/day_02_input.txt", "r") as f:
    intcode_program = [int(item) for item in f.read().split(",")]
    # before running the program,
    # replace position `1` with the value `12` and
    # replace position `2` with the value `2`
    intcode_program[1] = 12
    intcode_program[2] = 2

# check the results of the calculation
assert calculate_intcode_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert calculate_intcode_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert calculate_intcode_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert calculate_intcode_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

# use the calculator on the intcode program
results = calculate_intcode_program(intcode_program)

print(f"""
The value left at position 0 after the program halts is {results[0]}
""")
