from requests import get
from requests.status_codes import codes as HTTPStatusCode
from Hash import hash
from Bucket import Bucket
from Stats import Stats

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words.txt'
#ENGLISH_WORDS_URL = 'https://drive.google.com/u/5/uc?id=1K8b8XP71B--U-OTFx60NDGbOwUH5Hk9x&export=download'

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


def makeBuckets(paginas, nb):
    buckets = [Bucket(stats, False) for i in range(0, nb)]
    # 93310

    for i in range(0, len(paginas)):
        for j in range(0, len(paginas[i])):
            hashIndex = hash(paginas[i][j], nb)
            buckets[hashIndex].add((paginas[i][j], i))

    for i in buckets:
        i.countCollisions()

    return buckets

def searchOnBucket(key, buckets, paginas, nb):
    hashIndex = hash(key, nb)
    tupla = buckets[hashIndex].search(key)

    if tupla is not None:
        stats.setCusto(1)
        return searchOnPage(tupla, paginas)
    else:
        return "Palavra não encontrada."


def searchOnPage(tupla, paginas):

    for i in paginas[tupla[1]]:
        if tupla[0] is i:
            return f"Palavra '{i}' encontrada!"


if __name__ == '__main__':
    tabela = load_database()
    tabela.pop(-1)

    global stats
    stats = Stats()

    pageSize = 10
    paginas = makePages(tabela, pageSize)

    nb = len(tabela) // 5
    buckets = makeBuckets(paginas, nb)

    key = "a\r"
    print(searchOnBucket(key, buckets, paginas, nb))

    print(stats.overflows)

    # print(buckets)

    teste = set()
    print(tabela[-1])

    for i in tabela:
        teste.add(hash(i, nb))

    aux = [0 for i in range(0, len(buckets))]

    for i in range(0, len(tabela)):
        aux[hash(tabela[i], nb)] += 1

    print(max(aux), aux.index(max(aux)))

    print(len(tabela) / len(teste))

    print('tamanho do set ', len(teste))
    print('tamanho do database ', len(tabela))

    aux = 0

    for i in buckets:
        aux += len(i.registros)

    a = 0
