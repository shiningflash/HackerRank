#!/bin/python3

import os
import re


def minimumNumber(n, password):
    ans = 1 if not re.search('[0-9]+', password) else 0
    ans += 1 if not re.search('[a-z]+', password) else 0
    ans += 1 if not re.search('[A-Z]+', password) else 0
    ans += 1 if not re.search('[\!\@\#\$\%\^\&\*\(\)\-\+]+', password) else 0
    return ans + max(0, 6 - n - ans)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()
