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


# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) > n:
        final_str = s[:n]
        a_count = 0
        for f_s in list(final_str):
            if 'a' == f_s:
                a_count += 1
        return a_count
    else:
        each_a_count = 0
        for ss in list(s):
            if 'a' == ss:
                each_a_count += 1
        times = n // len(s)
        re = n % len(s)
        rest_str = s[:re]
        rest_count = 0
        for ss in list(rest_str):
            if 'a' == ss:
                rest_count += 1
        return each_a_count * times + rest_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
