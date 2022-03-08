from requests import get
from requests.status_codes import codes as HTTPStatusCode
from Hash import hash
from Bucket import Bucket
from Stats import Stats

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words.txt'


def loadDatabase():
    return getWordsFromRepo().text.split("\n")


def getWordsFromRepo():
    response = get(ENGLISH_WORDS_URL)

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Não foi possível obter a lista de palavras do repositório!'
        raise ValueError(invalid_response_error)

    return response


def makePages(tabela, pageSize):
    return [tabela[i:i + pageSize] for i in range(0, len(tabela), pageSize)]


def makeBuckets(paginas, nb):
    buckets = [Bucket(stats, False) for _ in range(nb)]
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
        stats.addCusto()
        return searchOnPage(tupla, paginas)

    return "Palavra não encontrada."


def searchOnPage(tupla, paginas):
    for i in paginas[tupla[1]]:
        if tupla[0] is i:
            return f"Palavra '{i}' encontrada!"


if __name__ == '__main__':
    tabela = loadDatabase()
    tabela.pop(-1)

    stats = Stats()

    pageSize = 10
    paginas = makePages(tabela, pageSize)

    nb = len(tabela) // 5
    buckets = makeBuckets(paginas, nb)

    key = "."
    print(searchOnBucket(key, buckets, paginas, nb))

    print(f"Overflows: {stats.overflows}")
    print(f"Custo: {stats.custo}")
    print(f"Collisions: {stats.collisions}")
