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


# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = list(s)
    tracks = [0 for _ in range(n + 1)]
    for idx, step in enumerate(steps):
        if "U" == step:
            tracks[idx + 1] = tracks[idx] + 1
        elif "D" == step:
            tracks[idx + 1] = tracks[idx] - 1

    zero_indexes = []
    for idx, t in enumerate(tracks):
        if t == 0:
            zero_indexes.append(idx)
    valley_count = 0
    for z_idx in zero_indexes:
        if z_idx == len(tracks) - 1:
            continue
        if tracks[z_idx + 1] < 0:
            valley_count += 1
    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
