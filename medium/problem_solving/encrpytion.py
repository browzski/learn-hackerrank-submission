#!/bin/python3
import math
'''
1. remove whitespace of n
2. make sqrt of it then find min() and max()
3. make multi dimensional array with the string based on :
    vertical = min()
    horizontal = max()
4. make sure min() * max() > n
5. get vertical array count from min() for max() time
'''


def encryption(s):
    s = s.replace(" ","")
    l = len(s)
    t = math.sqrt(l)
    up = math.ceil(t)
    down = math.floor(t)
    # print("up : {} | down : {} | length : {}".format(up, down, l))

    if(up * down < l):
        down = up
    arr = []
    res = ""
    num = 0
    for i in range(down):
        arr2 = []

        for ii in range(up):
            if(num >= l):
                break
            arr2.append(s[num])
            num += 1
        arr.append(arr2)
    # print(arr)

    for i in range(up):
        for ii in range(down):
            ll = len(arr[ii])-1
            if(ll < i):
                continue
            res += arr[ii][i]

            # print("[{}{}]".format(i,ll),end=" ")
            # print("|{}{}|{}".format(ii,i,num),end=" ")
        # print("")
        res += " "

    print(res)

    # print(arr)


if __name__ == '__main__':
    s = input()
    # s = "if man was meant to stay on the ground god would have given us roots"
    encryption(s)
