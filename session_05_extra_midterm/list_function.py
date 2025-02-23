"""
Write a function called general_poly, that meets the specifications below.
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗103+2∗102+3∗101+4∗100.

def general_poly (L):
     L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
"""


def general_poly(L):
    """L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0"""

    def evaluate(x):
        result = 0
        exponent = len(L) - 1  # Start with the highest exponent
        for coefficient in L:
            result += coefficient * (x**exponent)
            exponent -= 1  # Reduce exponent for the next term
        return result

    return evaluate


print(general_poly([1, 2, 3, 4])(100))
