from requests import get
from requests.status_codes import codes as HTTPStatusCode
from Hash import hash_function

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words.txt'


def load_database():
    content = retrieve_words_from_repo()
    data = content.text.split("\n")
    filtered_data = list(filter(len, data))
    return filtered_data


def retrieve_words_from_repo():
    response = get(ENGLISH_WORDS_URL)

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Não foi possível obter a lista de palavras do repositório!'
        raise ValueError(invalid_response_error)

    return response


if __name__ == '__main__':
    database = load_database()
    database.pop(-1)
    teste = set()
    print(database[-1])

    for i in database:

       teste.add(hash(i,len(database)))

    print('tamanho do set ', len(teste))
    print('tamanho do database ', len(database))

