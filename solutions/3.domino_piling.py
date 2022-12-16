import math

def pileDominos(m, n):
    result = (m * n)/2
    if(result % 2 == 0):
        result = result
    
    else:
        result = math.floor(result)
    
    print(result)



pileDominos(3, 3)