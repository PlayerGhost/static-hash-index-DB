def hash_function(word, bucket_size):
    ascii_word = list(map(ord, word))
    half_word_index = len(word) // 2
    print(word, word[half_word_index])

    result = ascii_word[half_word_index]

    result += sum([i for i in ascii_word[:half_word_index]])

    for i in range(half_word_index, len(word)):
        even_index = i % 2 == 0
        result += ascii_word[i] * (1 if even_index else -1)

    return abs(result % bucket_size)
