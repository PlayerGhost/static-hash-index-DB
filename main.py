import requests

def loadDatabase():
    rawData = requests.get('https://github.com/dwyl/english-words/raw/master/words_dictionary.json')
    dataDict = rawData.json()

    return list(dataDict.items())

if __name__ == '__main__':
    database = loadDatabase()

    print(database)
