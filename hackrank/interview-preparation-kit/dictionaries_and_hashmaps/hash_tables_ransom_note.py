#!/bin/python3

import math
import os
import random
import re
import sys

_LOCAL = False

if _LOCAL:
    os.environ['OUTPUT_PATH'] = 'output.txt'


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_words = {}
    for mag in magazine:
        if magazine_words.get(mag) is None:
            magazine_words[mag] = 0
        else:
            magazine_words[mag] += 1
    for n in note:
        if magazine_words.get(n) is None or magazine_words.get(n) < 0:
            print("No")
            return
        else:
            magazine_words[n] -= 1

    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
