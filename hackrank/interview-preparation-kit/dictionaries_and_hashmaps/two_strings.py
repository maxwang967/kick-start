#!/bin/python3

import math
import os
import random
import re
import sys

_LOCAL = False

if _LOCAL:
    os.environ['OUTPUT_PATH'] = 'output.txt'


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_locations = {}
    for c in list(s1):
        s1_locations[c] = True
    for c in list(s2):
        if s1_locations.get(c) is not None:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
