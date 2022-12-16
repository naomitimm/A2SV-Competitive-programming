import numpy as np
def countingSort(numbers):

    max = np.max(numbers)
    arr = [0 for _ in range(max + 1)]

    for number in numbers:
        arr[number] += 1
    
    print(arr)

countingSort([4, 1, 3, 4, 6, 6])


