from math import pi

def area_circle(r: int) -> int:
    """This function return the area of circle"""
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot negative.")
    return pi*(r**2)