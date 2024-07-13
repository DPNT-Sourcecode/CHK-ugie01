# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    # Check if both values are integers
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both values must be integers")

    # Check if both values are between 0 and 100
    elif x < 0 or x > 100 or y < 0 or y > 100:
        raise ValueError("Both values must be between 0 and 100")
    
    # Return the sum of x and y
    else:
        return x + y
