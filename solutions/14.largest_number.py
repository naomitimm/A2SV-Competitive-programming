def largestNumber(numbers):
    numbers = [str(num) for num in numbers]
    
    for n in range(len(numbers)):
        for m in range(len(numbers)):
            if(numbers[n] + numbers[m] < numbers[m] + numbers[n]):
                numbers[n] , numbers[m] = numbers[m] , numbers[n]

    numbers.reverse()
    result = "".join(numbers)

    print(result)
largestNumber([3,30,34,5,9])
