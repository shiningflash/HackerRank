#!/bin/python3

import os


def pickingNumbers(a):
    cnt = {}
    for i in range(0, 100): cnt[i] = 0
    for x in a: cnt[x] += 1
    mx = 0
    for i in range(0, 99):
        mx = max(mx, cnt[i] + cnt[i+1])
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
