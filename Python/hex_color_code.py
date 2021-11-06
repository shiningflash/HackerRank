import re
import sys


def is_hex_color_code(color):
    if re.search("^#[A-Fa-f0-9]{3}[^A-Fa-f0-9]*$", color):
        return color[:4]
    if re.search("^#[A-Fa-f0-9]{6}[^A-Fa-f0-9]*$", color):
        return color[:7]
    return None


def process(code):
    code = code.split('\n')
    code = [word for word in code if word.__contains__(':')]
    code = [word.replace(':#', ": #") for word in code]
    tmp = []
    for word in code:
        words = word.split(' ')
        for x in words:
            if x.__contains__('#'):
                tmp.append(x)
    colors = []
    for color in tmp:
        res = is_hex_color_code(color)
        if res:
            colors.append(res)
    return "\n".join(colors)
            

if __name__ == '__main__':
    code = "".join(sys.stdin.readlines())
    ans = process(code)
    print(ans)
