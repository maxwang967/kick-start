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


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for idx in range(len(q)):
        if q[idx] - (idx + 1) > 2:
            print("Too chaotic")
            return
        else:
            for j in range(max(0, q[idx] - 2), idx):
                if q[j] > q[idx]:
                    bribes += 1
    print(bribes)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
