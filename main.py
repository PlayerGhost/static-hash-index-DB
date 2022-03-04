from requests import get
from requests.status_codes import codes as HTTPStatusCode
from Hash import hash
from Bucket import Bucket
from Stats import Stats

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

    # valor do usuario
    pageSize = 10

    paginas = makePages(tabela, pageSize)

    nb = len(tabela) // 5
    buckets = [Bucket() for i in range(0, nb)]
    # print(nb)
    # print(buckets)
    # 93310

    for i in range(0, len(paginas)):
        for j in range(0, len(paginas[i])):
            hashIndex = hash(paginas[i][j], nb)
            buckets[hashIndex].add((paginas[i][j], i))

    # print(buckets)

    # teste = set()
    # print(tabela[-1])

    # for i in tabela:
    #    teste.add(hash(i, nb))

    # print(max(teste))

    # print(len(tabela) / len(teste))

    # print('tamanho do set ', len(teste))
    # print('tamanho do database ', len(tabela))
