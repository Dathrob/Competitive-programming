#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, array):
    stored_value = array[len(array)-1]
    size = n-1
    check = 0
    for i in range(size-1,-1,-1):
        if(array[i]>stored_value):
            array[i+1] = array[i]
            print(*array)
        else:
            array[i+1] = stored_value
            print(*array)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
