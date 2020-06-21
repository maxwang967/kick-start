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
from itertools import permutations

os.environ['OUTPUT_PATH'] = 'output.txt'


def checkDivisibility(arr):
    result_list = []
    for a in arr:
        perms = permutations(list(a))
        has_yes = False
        for p in perms:
            if int("".join(p)) % 8 == 0:
                result_list.append("YES")
                has_yes = True
                break
        if not has_yes:
            result_list.append("NO")
    return result_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    result = checkDivisibility(arr)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()