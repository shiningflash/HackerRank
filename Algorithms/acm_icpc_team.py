#!/bin/python3

import os


def acmTeam(topic):
    score = []
    n, m = len(topic), len(topic[0]) 
    for i in range(n-1):
        for j in range(i+1, n):
            tot = 0
            for k in range(m):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    tot += 1
            score.append(tot)
    mx = max(score)
    cnt = score.count(mx)
    return [mx, cnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    
    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
