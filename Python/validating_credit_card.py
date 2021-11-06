import re


def check_repeat(code) -> bool:
    prev, cnt = "", 0
    for c in code:
        if c == '-': continue
        if prev == c: cnt += 1
        else: cnt = 1
        if cnt >= 4: return False
        prev = c
    return cnt < 4


def is_valid(code) -> bool:
    return re.search("^[4-6][0-9]{3}[\-]{0,1}[0-9]{4}[\-]{0,1}[0-9]{4}[\-]{0,1}[0-9]{4}$", code) and check_repeat(code)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        code = input()
        print("Valid" if is_valid(code) else "Invalid")
