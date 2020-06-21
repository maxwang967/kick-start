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


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for _ in range(n)]
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        array[a - 1] += k
        if b < len(array):
            array[b] -= k
    max_num = x = 0
    for i in array:
        x = x + i
        if max_num < x:
            max_num = x
    return max_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
