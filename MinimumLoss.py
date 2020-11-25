#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.



if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().strip().split()))
    arr = [(p[i], i) for i in range(n)]

    arr.sort(reverse=True)
    res = arr[0][0]
    for i in range(n - 1):
        p1 = arr[i]
        p2 = arr[i + 1]
        if p1[0] > p2[0] and p1[1] < p2[1]:
            if (p1[0] - p2[0] < res):
                res = p1[0] - p2[0]
    print(res)
