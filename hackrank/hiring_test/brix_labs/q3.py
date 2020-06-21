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

# a e i o u
locations = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 3,
    "u": 4
}

vowels = list("aeiou")


def get_subsequence(current_str, sub_str, idx):
    if idx == len(current_str):
        for v in vowels:
            if v not in sub_str:
                return []
        return sub_str
    else:
        if len(sub_str) == 0:
            if current_str[idx] != 'a':
                return get_subsequence(current_str, sub_str, idx + 1)
            else:
                return get_subsequence(current_str, sub_str + [current_str[idx]], idx + 1)
        elif locations[current_str[idx]] == locations[sub_str[-1]]:
            return get_subsequence(current_str, sub_str + [current_str[idx]], idx + 1)
        elif locations[current_str[idx]] == (locations[sub_str[-1]] + 1):
            str1 = get_subsequence(current_str, sub_str + [current_str[idx]], idx + 1)
            str2 = get_subsequence(current_str, sub_str, idx + 1)
            return str1 if len(str1) > len(str2) else str2
        else:
            return get_subsequence(current_str, sub_str, idx + 1)


def longestVowelSubsequence(s):
    return len(get_subsequence(s, [], 0))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = longestVowelSubsequence(s)

    fptr.write(str(result) + '\n')

    fptr.close()
