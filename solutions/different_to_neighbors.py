def differentToAvgOfNeighbors(numbers):
    numbers.sort()
    for number in range(0,len(numbers)-1):
        if((numbers[number - 1] + numbers[number + 1])/2 == numbers[number]):
            numbers[number - 1] , numbers[number] = numbers[number] , numbers[number - 1]


    print(numbers)

differentToAvgOfNeighbors([6,2,0,9,7])