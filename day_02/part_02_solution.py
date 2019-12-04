"""
To complete the gravity assist, you need to determine
what pair of inputs produces the output 19690720
"""
from part_01_solution import calculate_intcode_program

# load necessary data
with open("data/day_02_input.txt", "r") as f:
    intcode_program = [int(item) for item in f.read().split(",")]

# start the brute force inspection for the right pair
for noun in range(100):
    for verb in range(100):
        # before running the program,
        # replace position `1` with the value noun and
        # replace position `2` with the value verb
        intcode_program[1] = noun
        intcode_program[2] = verb
        # use the calculator on the intcode program
        results = calculate_intcode_program(intcode_program)
        # check if position `0` contains the desired value
        if results[0] == 19690720:
            print(f"results = {results[0]}")
            print(f"noun = {noun}")
            print(f"verb = {verb}")
            print(f"""
            The value of 100 * {noun} + {verb} is {100 * noun + verb}
            """)
            break
        else:
            continue
