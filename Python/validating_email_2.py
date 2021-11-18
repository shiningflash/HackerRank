def isalphabet(c):
    return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

def isalphaneumeric(c):
    return isalphabet(c) or '0' < c <= '9'

def isalphanumsign(c):
    return isalphaneumeric(c) or c in ['_', '-']

def fun(s):
    pos, ext = 0, 0
    if s[0] == '@': return False
    for c in s:
        if c == '@' and pos == 0: pos = 1; continue
        if c == '.' and pos == 1: pos = 2; continue
        if pos == 0:
            if not isalphanumsign(c):
                return False
            continue
        if pos == 1:
            if not isalphaneumeric(c):
                return False
            continue
        if pos == 2:
            ext += 1
            if not isalphabet(c) or ext > 3:
                return False
                return 
            continue
    return pos == 2

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
