# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 1:11 下午
# @Author  : morningstarwang
# @FileName: sock_merchant.py
# @Blog: wangchenxing.com


# !/bin/python3

import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'output.txt'


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_counter = {}
    avalible_pair_count = 0
    for color in ar:
        color_counter[color] = 0
    for color in ar:
        color_counter[color] += 1
    for color_key in color_counter.keys():
        avalible_pair_count += (color_counter[color_key] - color_counter[color_key] % 2) // 2
    return avalible_pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
