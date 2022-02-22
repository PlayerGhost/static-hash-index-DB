from requests import get
from requests.status_codes import codes as HTTPStatusCode

ENGLISH_WORDS_URL = 'https://github.com/dwyl/english-words/raw/master/words_dictionary.json'


def load_database():
    wordlist_json = get_words_from_repo()
    result = wordlist_json.keys()

    return result


def get_words_from_repo():
    response = get(ENGLISH_WORDS_URL)

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Não foi possível obter a lista de palavras do repositório!'
        raise ValueError(invalid_response_error)

    return response.json()


if __name__ == '__main__':
    database = load_database()

    print(database)
