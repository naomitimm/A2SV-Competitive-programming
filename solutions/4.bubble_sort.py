#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    l = len(a)
    swaps = 0
    for i in range(l):
        for j in range(l - 1):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps+=1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
    return 

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
