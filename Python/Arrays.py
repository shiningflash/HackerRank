import numpy


def arrays(arr):
    arr = list(map(float, arr))
    arr = numpy.array(arr)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
