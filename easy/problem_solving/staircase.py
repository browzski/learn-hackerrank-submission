#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(n,0,-1):
        for a in range(n):
            #print("i : {} and a : {}".format(i,a))
            if(a < i-1):
                #print("if : {}".format(a))
                print(" ",end="")
            else:
                #print("else : {}".format(i))
                print("#",end="")
        print("")


    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
