import math

def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"({x1}, {x2})"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"({x})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {c}"


def derivation(a, b, c):
    da = 2*a
    db = b
    if da != 0 and db != 0:
        return f"f'(x) = {da} * X + {db}"
    elif da == 0 and db != 0:
        return f"f'(x) = {db}"
    elif da != 0 and db == 0:
        return f"f'(x) = {da} * X"
    else:
        return "f'(x) = 0"