from collections import deque


def work():
    n = int(input())
    arr = deque(map(int, input().split()))
    mx = 1 << 31
    for i in range(n):
        left = arr[0]
        right = arr[-1]
        if max(left, right) > mx:
            return "No"
        if left > right:
            mx = left
            arr.popleft()
        else:
            mx = right
            arr.pop()
    return "Yes"

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(work())
