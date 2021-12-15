import re

if __name__ == '__main__':
    sen = " ".join([input() for _ in range(int(input()))])
    for _ in range(int(input())):
        regex = '(?<!\w){0}(?!\w)'.format(input())
        pattern = re.compile(regex)
        print(len(re.findall(pattern, sen)))
