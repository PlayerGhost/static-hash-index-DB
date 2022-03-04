
def hash(registro, bucketSize):

    index = len(registro) // 2
    half = ord(registro[index])

    for i in range(index, len(registro)):
        if i % 2 == 0:
            half = (half + ord(registro[i])*2)*i
        else:
            half = (half - int(ord(registro[i])/3))*i

    for j in range(0, index):
        half += ord(registro[j])

    return int(abs(half % bucketSize))
