def solve(r):
    s = list(r)
    s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] is ' ':
            s[i] = s[i].upper()
    print(''.join(s))

if __name__ == '__main__':
    s = raw_input()
    solve(s)
