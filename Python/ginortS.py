if __name__ == '__main__':
    S = input()
    sml = ''.join(sorted([x for x in S if x.islower()]))
    cap = ''.join(sorted([x for x in S if x.isupper()]))
    odd = ''.join(sorted([x for x in S if x.isnumeric() if int(x) % 2 == 1]))
    eve = ''.join(sorted([x for x in S if x.isnumeric() if int(x) % 2 == 0]))
    print(''.join([sml, cap, odd, eve]))
