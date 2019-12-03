"""
To complete the gravity assist, you need to determine
what pair of inputs produces the output 19690720
"""
from part_01_solution import calculate_intcode_program

for noun in range(0, 100):
    for verb in range(0, 100):
        with open("data/day_02_input.txt", "r") as f:
            intcode_program = [int(item) for item in f.read().split(",")]
            # before running the program,
            # replace position `1` with the value noun and
            # replace position `2` with the value verb
            intcode_program[1] = noun
            intcode_program[2] = verb
        # print(f"first 5 of IP: {intcode_program[0:5]}")
        # use the calculator on the intcode program
        results = calculate_intcode_program(intcode_program)
        # print(f"first 5 of results: {results[0:5]}")
        # print(f"The value left at position 0 after the program halts is {results[0]}")
        if results[0] == 19690720:
            break
        else:
            continue

print(f"noun = {noun}")
print(f"verb = {verb}")
print(f"""
The value of 100 * {noun} + {verb} is {100 * noun + verb}
""")
