
def binary_search(target: int, data: list[int]) -> int | None:
    low: int = 0
    hight: int = len(data) - 1

    while low < hight:
        mid: int = (low + hight) // 2
        guess: int = data[mid]

        if guess == target:
            return f"Found {target} at index {mid}"
        
        if guess > target:
            hight = mid - 1
        
        else:
            low = mid + 1
        
    return None


if __name__ == '__main__':
    data: list[int] = [x for x in range(1, 190, 3)]
    target: int = 184

    print(binary_search(target, data))