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


def getMin(s):
    parentless_counter = {
        "left": 0,
        "right": 0
    }
    characters = list(s)
    for c in characters:
        if "(" == c:
            parentless_counter["left"] += 1
        elif ")" == c:
            parentless_counter["right"] += 1
    return abs(parentless_counter["left"] - parentless_counter["right"])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMin(s)

    fptr.write(str(result) + '\n')

    fptr.close()