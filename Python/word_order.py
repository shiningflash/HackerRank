if __name__ == '__main__':
    n = int(input())

    mp = {}

    for i in range(n):
        word = input()
        if word in mp:
            mp[word] += 1
        else:
            mp[word] = 1
            
    length = len(mp)
    print(length)
    
    for word in mp:
        print(mp[word], end=' ' if length > 1 else '\n')
