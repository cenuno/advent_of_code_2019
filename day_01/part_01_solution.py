"""
Given the mass of each module, 
calculate the sum of the fuel requirement for all modules
"""


def calculate_fuel(x: int) -> int:
    """Given the mass of a module, calculate the fuel requirement
    Args:
        - x (int): the mass of the module

    Returns:
        int: the fuel requirement for the module

    Examples:
    For a mass of 12, divide by 3 and round down to get 4, then sub 2 to get 2.
    For a mass of 14, dividing by 3 and round down yields 4 to also get 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    """
    return (x // 3) - 2


# quick gut check that the function is correct
assert calculate_fuel(x=12) == 2
assert calculate_fuel(x=14) == 2
assert calculate_fuel(x=1969) == 654
assert calculate_fuel(x=100756) == 33583

# load data
with open("data/day_01_input.txt", "r") as f:
    module_masses = f.read().split("\n")

# find the fuel requirement for each module
fuel_requirement = [calculate_fuel(x=int(mass))
                    for mass in module_masses]

# print the sum of the fuel requirement for all the modules
print(f"""
The sum of the fuel requirement for all modules is {sum(fuel_requirement)}
""")

# end of script #
