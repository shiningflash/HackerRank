if __name__ == '__main__':
    # input
    n, m = map(int, input().split())
    arr = map(int, input().split())
    A = map(int, input().split())
    B = map(int, input().split())

    # dictionary
    mpa, mpb = {}, {}
    for x in A:
        mpa[x] = True
    for x in B:
        mpb[x] = True

    happiness = 0

    # count happiness
    for x in arr:
        if x in mpa:
            happiness += 1
        if x in mpb:
            happiness -= 1

    print(happiness)
