
"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    
    for a_s,b_s in zip(a,b):
        if a_s == b_s:
            continue
        elif a_s > b_s:
            alice += 1
        elif a_s < b_s:
            bob += 1
    
    # print(f'{alice} {bob}')
    return [alice,bob]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
