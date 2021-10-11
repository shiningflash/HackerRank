def print_formatted(number):
    max_len = len(bin(number)[2:])
    for num in range(1, number+1):
        print((str(num).rjust(max_len)), end=' ')
        print((oct(num)[2:].rjust(max_len)), end=' ')
        print((hex(num)[2:].rjust(max_len)).upper(), end=' ')
        print((bin(num)[2:].rjust(max_len)), end=' ')
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
