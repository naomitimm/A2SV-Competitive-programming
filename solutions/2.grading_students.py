def studentGrading(grades):
    result = []
    for grade in grades:
        rounder = 5 - (grade % 5)
        if(grade < 38):
            result.append(grade)
        elif (rounder < 3):
            grade += rounder
            result.append(grade)
        else:
            result.append(grade)
    
    print(result)
 

number = [73, 67, 38, 33]

studentGrading(number)
