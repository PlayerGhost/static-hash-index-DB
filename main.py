import requests

    if response.status_code != HTTPStatusCode.OK:
        invalid_response_error = 'Houve algum erro durante a obtenção dos dados'
        raise ValueError(invalid_response_error)

    return list(dataDict.items())

if __name__ == '__main__':
    database = loadDatabase()

    print(database)
