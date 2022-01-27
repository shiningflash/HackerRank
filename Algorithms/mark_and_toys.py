#!/bin/python3

import os


def maximumToys(prices, k):
    prices = sorted(prices)
    sum, cnt = 0, 0
    for x in prices:
        sum += x
        if sum > k: break
        cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
