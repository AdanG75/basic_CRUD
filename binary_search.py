import random
from typing import Optional


def binary_search(data: list, target: int, begin: int, last: int) -> Optional[int]:
    if last < begin:
        return False

    actual_index = (begin + last) // 2
    
    print(actual_index)
    if data[actual_index] == target:
        return True
    elif data[actual_index] < target:
        return binary_search(data, target, actual_index + 1, last)
        
    else:
        return binary_search(data, target, begin, actual_index - 1)


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(100)]
    data.sort()

    print(data)
    target = int(input('What nomber would you like to find?:\n-> '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)