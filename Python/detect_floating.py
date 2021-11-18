import re


def isFloat(n):
    return re.fullmatch("^[+-]{0,1}[0-9]*\.[0-9]{1,}$", n)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        print(True if isFloat(n) else False)
