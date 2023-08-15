
def sum_elements(elements: list):
    """Sum elements of a list"""
    sum = 0
    if len(elements) == 0:
        return 0
    else:
        sum = elements[0] + sum_elements(elements[1:])


def count_numbers(elements: list):
    """Count the number of elements in a list"""
    count = 0
    if len(elements) == 0:
        return 0
    else:
        count = 1 + count_numbers(elements[1:])

    return count





if __name__ == "__main__":
    print(count_numbers([1,2,3,4,5]))
