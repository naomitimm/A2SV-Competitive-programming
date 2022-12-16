def findTargetIndice(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j] , numbers[j + 1] = numbers[j + 1] , numbers[j]

    result = []
    for number in range(len(numbers)):
        if(numbers[number] == target):
            result.append(number)

    print(result)

findTargetIndice([1,2,5,2,3], 3)