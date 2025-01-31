# Automatize limit tabulation
from math import sqrt, sin, cos

ratio = [
    -0.1,
    -0.01,
    -0.001,
    0,
    0.001,
    0.01,
    0.1
]

def formula(x):
    try:
        """

        Note:
        For every polynomial expression, please put parentheses
        Example:
        2/x-5 -> 2/(x-5)

        """
        formula = 2/(x-5)
        
        return formula

    except ZeroDivisionError:
        pass



value: int = int(input("Reference value: "))
print("\n")

for variation in ratio:
    number: float = value+variation
    print(f"f({number}): {formula(number)} \n")



