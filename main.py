from requests import get
from requests.status_codes import codes as HTTPStatusCode
from Hash import hash

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words.txt'


def load_database():
    return get_words_from_repo().text.split("\n")


def get_words_from_repo():
    response = get(ENGLISH_WORDS_URL)

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Não foi possível obter a lista de palavras do repositório!'
        raise ValueError(invalid_response_error)

    return response


def makePages(tabela, pageSize):
    return [tabela[i:i + pageSize] for i in range(0, len(tabela), pageSize)]


if __name__ == '__main__':
    tabela = load_database()
    tabela.pop(-1)

    pageSize = 10
    paginas = makePages(tabela, pageSize)

    nb = len(tabela) // 5
    buckets = [[None for i in range(0, 5)] for i in range(0, nb)]
    # print(nb)
    # print(buckets)
    # 93310

    for i in range(0, len(paginas)):
        for j in range(0, len(paginas[i])):
            hashIndex = hash(paginas[i][j], nb)

            if buckets[hashIndex][-1] is not None:
                hasSlot = False

                for k in range(0, len(buckets[hashIndex])):
                    if hasSlot:
                        break

                    if type(buckets[hashIndex][k]) == list:
                        if len(buckets[hashIndex]) == 7:
                            aux = 0

                        for l in range(0, len(buckets[hashIndex][k])):
                            if buckets[hashIndex][k][l] is None:
                                buckets[hashIndex][k][l] = (paginas[i][j], i)
                                hasSlot = True
                                break

                if not hasSlot:
                    bucketOverflow = [None for i in range(0, 5)]
                    bucketOverflow[0] = (paginas[i][j], i)

                    buckets[hashIndex].append(bucketOverflow)
            else:
                for k in range(0, len(buckets[hashIndex])):
                    if buckets[hashIndex][k] is None:
                        buckets[hashIndex][k] = (paginas[i][j], i)
                        break

    aux = [0 for i in range(0, len(buckets))]

    for i in range(0, len(tabela)):
        aux[hash(tabela[i], nb)] += 1

    print(max(aux), aux.index(max(aux)))

    print(buckets[aux.index(max(aux))])

    #print(buckets)

    # teste = set()
    # print(tabela[-1])

    # for i in tabela:
    #    teste.add(hash(i, nb))

    # print(max(teste))

    # print(len(tabela) / len(teste))

    # print('tamanho do set ', len(teste))
    # print('tamanho do database ', len(tabela))
