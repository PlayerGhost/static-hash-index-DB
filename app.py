from json import dumps as dictAsString
from flask import Flask, request, Response
from flask_cors import CORS

from main import Programa

app = Flask(__name__)
programa = Programa()
CORS(app)


def newResponse():
    res = Response()
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route("/")
def main():
    response = newResponse()

    try:
        parametroTamanhoPagina = request.args.get('pageSize', None)
        if parametroTamanhoPagina is None:
            undefinedPageSizeErr = "Não foi definido um tamanho de página"
            raise ValueError(undefinedPageSizeErr)

        tamanhoPagina = int(parametroTamanhoPagina)
        programa.stats.reset()
        programa.setup(tamanhoPagina)
        response.status = 200

        successfulDatabaseSetup = f"Banco de dados com tamanho de página: {tamanhoPagina}"
        return successfulDatabaseSetup

    except ValueError as err:
        response.status = 500
        response.set_data(inBytes(repr(err)))

    return response


@app.route("/search")
def search():
    response = newResponse()

    try:
        palavra = request.args.get('wordToSearch', None)
        if palavra is None:
            raise ValueError("Palavra não fornecida!")

        response.status = 200

        result = programa.searchOnBucket(palavra)
        response.set_data(inBytes(dictAsString(result)))

    except ValueError as err:
        response.status = 500
        response.set_data(inBytes(repr(err)))

    return response


@app.route("/health")
def health():
    response = newResponse()
    response.status = 200
    return "ok"


@app.route("/stats")
def stats():
    response = newResponse()
    response.status = 200
    currentStats = programa.stats.get()

    response.set_data(inBytes(dictAsString(currentStats)))
    return response


def inBytes(content):
    return content.encode('utf8')


if __name__ == '__main__':
    app.run()
