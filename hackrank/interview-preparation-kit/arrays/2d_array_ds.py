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

os.environ['OUTPUT_PATH'] = 'output.txt'


# Complete the hourglassSum function below.
def hourglassSum(arr):
    # i = 0, 1, 2, 3
    # j = 0, 1, 2, 3
    sum_array = [0 for _ in range(16)]
    idx = 0
    for i in range(4):
        for j in range(4):
            sum_array[idx] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + \
                             arr[i + 2][j] + arr[i + 2][j + 2]
            idx += 1
    return max(sum_array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
