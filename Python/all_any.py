if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    print(all([all([int(x) > 0 for x in arr]), any([x == x[::-1] for x in arr])]))
