def hash_function(word, bucket_size):
    ascii_word = list(map(ord, word))
    half_word_index = len(word) // 2
    print(word, word[half_word_index])

    result = ascii_word[half_word_index]

    index = math.trunc(len(registro) / 2)
    half = ord(registro[index])
    print(registro,registro[index])

    for i in range(index + 1, len(registro)):
        if i % 2 == 0:
            half = half + ord(registro[i])
        else:
            half = half - ord(registro[i])

    for j in range(0, index):
        half += ord(registro[j])

    return abs(half % bucketSize)
