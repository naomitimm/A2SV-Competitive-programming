def smallerNumberThanCurrent(numbers):
    sorted = [0 for _ in range(len(numbers))]
    for number in range(len(numbers)):
        print(numbers[number])
        for i in range(len(numbers)):
            if(numbers[number] > numbers[i]):
                sorted[number] += 1

    print(sorted)

smallerNumberThanCurrent([6,5,4,8])