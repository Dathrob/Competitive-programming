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
    count = 0
    sorted = False
    last_element  = len(a)-1
    while not sorted:
        sorted = True
        for i in range(0,len(a)-1):
            if a[i] > a[i+1]:
                sorted = False
                a[i],a[i+1] = a[i+1],a[i]
                count += 1
                
    print("Array is sorted in",count ,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[last_element])
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
