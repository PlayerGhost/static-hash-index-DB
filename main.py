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


if __name__ == '__main__':
    database = load_database()
    teste = set()

    '''for i in database:

       teste.add(hash(i,len(database)))

    print('tamanho do set ', len(teste))
    print('tamanho do database ', len(database))'''
