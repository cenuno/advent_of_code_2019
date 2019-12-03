"""
Calculate the sum of the fuel requirements for all of the modules
on your spacecraft when also taking into account the mass of the added fuel
"""


def _general_fuel_checker(mass: int) -> int:
    """Given the mass of a module, calculate the fuel requirement
    Args:
        - mass (int): the mass of the module

    Returns:
        int: the fuel requirement
    """
    return (mass // 3) - 2


def calculate_fuel(mass: int) -> int:
    """Given the mass of a module, calculate the total fuel requirement
    This calculation takes the initial fuel requirement as the input mass and
    repeat the process, continuing until a fuel requirement is zero or negative

    Args:
        - mass (int): the mass of the module

    Returns:
        int: the total fuel requirement for the module

    Examples:
    A module of mass 14 requires 2 fuel.
        This fuel requires no further fuel
        (2 divided by 3 and rounded down is 0,
        which would call for a negative fuel),
        so the total fuel required is still just 2.

    At first, a module of mass 1969 requires 654 fuel.
        Then, this fuel requires 216 more fuel (654 / 3 - 2).
        216 then requires 70 more fuel, which requires 21 fuel,
        which requires 5 fuel, which requires no further fuel.
        So, the total fuel required for a module of mass 1969 is
        654 + 216 + 70 + 21 + 5 = 966.

    The fuel required by a module of mass 100756 and its fuel is:
    33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
    """
    # calculate initial fuel requirement
    initial_fuel_req = _general_fuel_checker(mass)

    # inspect if the result of accounting for the next fuel requirement is <= 0
    if _general_fuel_checker(initial_fuel_req) <= 0:
        # no need to inspect further, return the results as is
        return initial_fuel_req
    else:
        # if the inspection fails, that means we can continue to add more fuel

        # store all fuel requirements in an empty list
        output = []
        output.append(initial_fuel_req)

        # inspect for two conditions:
        # 1. the latest fuel requirement is a value larger than zero; and
        # 2. calculating the next fuel requirement
        #    from the latest fuel requirement
        #    results in a value larger than zero
        while (output[-1] > 0) and (_general_fuel_checker(output[-1]) > 0):
            # if it passes, add the results to the output object
            output.append(_general_fuel_checker(output[-1]))
        # once the conditions are no longer met, return the sum of the results
        return sum(output)


# quick gut check that the function is correct
assert calculate_fuel(mass=14) == 2
assert calculate_fuel(mass=1969) == 966
assert calculate_fuel(mass=100756) == 50346

# load data
with open("data/day_01_input.txt", "r") as f:
    module_masses = [int(item) for item in f.read().split("\n")]

# find the fuel requirement for each module
fuel_requirement = [calculate_fuel(mass)
                    for mass in module_masses]

# print the sum of the fuel requirement for all the modules
print(f"""
The sum of the fuel requirement for all modules is {sum(fuel_requirement)}
""")

# end of script #
