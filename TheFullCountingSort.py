#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    ar = []
    for i in range(0, n):
        data = input().strip().split(' ')
        ar.append((int(data[0]), data[1]))
    arrCount = [0]*100
    for a in ar:
        arrCount[a[0]] += 1

    arrPositon = [0]*100
    for x in range(1, 100):
        arrPositon[x] = arrPositon[x-1] + arrCount[x-1]
    output = ['-']*n
    for i in range(0, n):
        if i >= n/2:
            output[arrPositon[ar[i][0]]] = ar[i][1]
        arrPositon[ar[i][0]] += 1
    print(' '.join(output))
