# E-1.1
def is_multiple(n: int, m: int) -> bool:
    """Return True if n is a multiple of m."""
    return n % m == 0


# E-1.2
def is_even(k: int) -> bool:
    """Return True if k is even."""
    return k & 1 == 0


# E-1.3
def minmax(data: list) :
    aux = 0
    for num in data:
        if data[num] > aux:
            aux = data[num]
