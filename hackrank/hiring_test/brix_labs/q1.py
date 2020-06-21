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


def isPrime(n):
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return 1
    else:
        return divisors[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = isPrime(n)

    fptr.write(str(result) + '\n')

    fptr.close()