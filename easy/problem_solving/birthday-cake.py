
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles = [3,2,1,3,4,4,4,4,4]
    candles.sort()
    a = 0
    for i in range(len(candles)):
        if i == 0 :
            continue

        if candles[i-1] < candles[i]:
            a = 1

        if candles[i-1] == candles[i]:
            a += 1
    
    print(a)


        
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout 
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
