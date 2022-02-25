import math


def hash(registro, bucketSize):

    index = math.trunc(len(registro) / 2)
    half = ord(registro[index])

    for i in range(index + 1, len(registro)):
        if i % 2 == 0:
            half = half + ord(registro[i])
        else:

            half = half - ord(registro[i])

    for j in range(0, index):
        half += ord(registro[j])

    return abs(half % bucketSize)
