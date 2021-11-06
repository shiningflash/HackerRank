import numpy as np


def find_min_and_max(arr):
    mn_arr = np.min(arr, axis=1)
    return np.max(mn_arr)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr = np.array(arr)
    ans = find_min_and_max(arr)
    print(ans)
