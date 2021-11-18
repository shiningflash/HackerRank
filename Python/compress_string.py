import math


def string_format(num, cnt) -> str:
    return "(" + str(cnt) + ", " + str(num) + ")"


def get_compression(x) -> str:
    ans = []
    num, cnt = "", 0
    for c in x:
        if num != "" and num != c:
            ans.append(string_format(num, cnt))
            cnt = 1
        else:
            cnt += 1
        num = c
    ans.append(string_format(num, cnt))
    return " ".join(ans)


if __name__ == '__main__':
    x = input()
    ans = get_compression(x)
    print(ans)
