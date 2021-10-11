if __name__=="__main__":
    s = list(input())
    x, y = input().split()
    s[int(x)] = y
    print(''.join(s))