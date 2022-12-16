def fizzBuzz(n):
    ls = []
    for number in range(n):
        if (number + 1) % 3 == 0 and (number + 1) % 5 == 0:
            ls.append("FizzBuzz")
        elif (number + 1) % 3 == 0:
            ls.append("Fizz")
        elif (number + 1) % 5 == 0:
            ls.append("Buzz")
        else :
            ls.append(str(number + 1))
    
    print(ls)

fizzBuzz(16)