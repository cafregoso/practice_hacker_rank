"""
    Rotate 'n' times the first element of an array to the end of the array.

    Constraints:
    -> 1 <= n <= 10^5
    -> 1 <= d <= n
    -> 1 <= arr[i] <= 10^6
"""

def left_rotation(arr:list[int], n: int) -> list[int]:
    """
        Rotate 'n' times the first element of an array to the end of the array.

        Args:
            arr (list[int]): Array to rotate.
            n (int): Number of times to rotate the array.

        Returns:
            list[int]: Rotated array.
    """
    for _ in range(n):
        arr.append(arr.pop(0))
    return arr

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    number_of_rotations = 54

    print(left_rotation(array, number_of_rotations))