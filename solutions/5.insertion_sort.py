def insertionSort(numbers):
    for index in range(1, len(numbers)):
        current = numbers[index]
        previous = index - 1

        while(previous >= 0 and numbers[previous] > current):
            (numbers[previous], numbers[previous + 1]) = (numbers[previous + 1], numbers[previous])
            previous = previous - 1

    print(numbers)

nums = [3, 1, 8, 6, 2]
insertionSort(nums)
        
        
            
