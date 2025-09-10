def square(number):
    constraints = [number < 1, number > 64]
    if any(constraints):
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 ** (number - 1)


def total():
    return 2**64-1
    pass
