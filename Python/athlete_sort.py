#!/bin/python3


def athlete_sort(n, m, arr, k):
    return sorted(arr, key=lambda x: x[k])


def print_arr(n, m, arr):
    for x in arr:
        print(' '.join(str(y) for y in x))


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorted_arr = athlete_sort(n, m, arr, k)
    print_arr(n, m, sorted_arr)
