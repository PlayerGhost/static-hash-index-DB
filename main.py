from requests import get
from requests.status_codes import codes as HTTPStatusCode

from Bucket import Bucket
from Hash import hash
from Stats import Stats

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words.txt'


def loadDatabase():
    content = getWordsFromRepo().text.split("\n")
    filtered_content = content[:-1]
    return filtered_content


def getWordsFromRepo():
    response = get(ENGLISH_WORDS_URL)

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Não foi possível obter a lista de palavras do repositório!'
        raise ValueError(invalid_response_error)

    return response


def makePages(tabela, pageSize):
    return [tabela[i:i + pageSize] for i in range(0, len(tabela), pageSize)]


def searchOnPage(tupla, paginas):
    for i in paginas[tupla[1]]:
        if tupla[0] is i:
            return {
                'res': f"Palavra {i} encontrada!",
                'page': tupla[1]
            }


class Programa:
    def __init__(self):
        self.stats = Stats()
        self.bucketSize = 10  # Predefinido
        self.tabela = loadDatabase()

        self.buckets = None
        self.paginas = None

    def setup(self, pageSize):
        self.paginas = makePages(self.tabela, pageSize)

        self.numeroBuckets = len(self.tabela) // self.bucketSize

        self.buckets = self.makeBuckets()

    def makeBuckets(self):
        buckets = [Bucket(self.stats, False, self.bucketSize)
                   for _ in range(self.numeroBuckets)]

        for i in range(0, len(self.paginas)):
            for j in range(0, len(self.paginas[i])):
                hashIndex = hash(self.paginas[i][j], self.numeroBuckets)
                buckets[hashIndex].add((self.paginas[i][j], i))

        for i in buckets:
            i.countCollisions()

        return buckets

    def searchOnBucket(self, key):
        hashIndex = hash(key, self.numeroBuckets)
        tupla = self.buckets[hashIndex].search(key)

        if tupla is not None:
            self.stats.addCusto()
            return searchOnPage(tupla, self.paginas)

        return "Palavra não encontrada."
