# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 1:11 下午
# @Author  : morningstarwang
# @FileName: sock_merchant.py
# @Blog: wangchenxing.com
import math
import os
import random
import re
import sys
from copy import deepcopy

os.environ['OUTPUT_PATH'] = 'output.txt'


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    locations = {}
    for idx in range(n):
        locations[arr[idx]] = idx
    for i in range(n):
        if arr[i] == i + 1:
            continue
        j = locations[i + 1]
        swaps += 1
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        locations[arr[i]] = i
        locations[arr[j]] = j
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
