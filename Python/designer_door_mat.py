def print_design_door(n, m):
    for i in range(1, n, 2):
        print((i*".|.").center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n-2, -1, -2):
        print((i*".|.").center(m, '-'))

if __name__ == '__main__':
    n, m = map(int, input().split())
    print_design_door(n, m)
