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


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    safe_clouds = []
    tracks = []
    for idx, cc in enumerate(c):
        if cc == 0:
            safe_clouds.append(idx)
    for idx in range(len(safe_clouds)):
        print(idx)
        print(tracks)
        if idx == 0:
            tracks.append(safe_clouds[0])
            continue
        if tracks[len(tracks) - 1] + 2 in safe_clouds:
            tracks.append(tracks[len(tracks) - 1] + 2)
        elif tracks[len(tracks) - 1] + 1 in safe_clouds:
            tracks.append(tracks[len(tracks) - 1] + 1)
    return len(tracks) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
