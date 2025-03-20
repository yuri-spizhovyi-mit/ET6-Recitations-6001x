def sum_digits(s):
    """Assumes s is a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s, it raises a ValueError exception."""

    list_of_digits = []
    for char in s:
        if char.isdigit():
            list_of_digits.append(int(char))
    if len(list_of_digits) > 0:
        return sum(list_of_digits)
    else:
        raise ValueError("No digits found in the string.")
