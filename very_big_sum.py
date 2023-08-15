"""
    -> arr[n]: list[int]

    Constrains
    -> 1 <= n <= 10
    -> 0 <= arr[1] <= 10**10
"""

def main(arr: list[int]) -> int:
    return sum(arr)

if __name__ == '__main__':
    arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(main(arr))