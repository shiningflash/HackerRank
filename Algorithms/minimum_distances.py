#!/bin/python3

import os


def minimumDistances(a):
    mp = {}
    ans = 10000
    for i, x in enumerate(a):
        if x in mp: ans = min(ans, i-mp[x])
        else: mp[x] = i
    return ans if ans != 10000 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
