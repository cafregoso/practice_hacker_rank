"""
    This is a staircase of size n = 4

    -> n: int
    -> 1 <= n <= 100
"""

def staircase(n: int) -> None:
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)


if __name__ == '__main__':
    n = 10
    staircase(n)
