#!/bin/python3

import os


def gameOfThrones(s):
    mp = {}
    for c in s:
        if c in mp: mp[c] += 1
        else: mp[c] = 1
    odd = 0
    for c in mp:
        if mp[c] % 2 == 1:
            odd += 1
    return "YES" if odd <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()
