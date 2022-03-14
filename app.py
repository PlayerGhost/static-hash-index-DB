import json
from urllib import response
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
    response = new_response()

    try:
        tamanhoPagina = int(request.args.get('pageSize', None))
        programa.stats.reset()
        programa.setup(tamanhoPagina)
        response.status = 200
        return "database initialized with page size: "+str(tamanhoPagina)
    except ValueError:
        response.status = 500

    return response


@app.route("/search")
def search():
    response = new_response()

    try:
        palavra = request.args.get('wordToSearch', None)
        if palavra is None:
            raise ValueError("Palavra não fornecida!")

        response.status = 200

        result = programa.searchOnBucket(palavra)
        response.set_data(dumps(result).encode('utf8'))


    except ValueError:
        response.status = 500
    
    return response


@app.route("/health")
def health():
    response = new_response()
    response.status = 200
    return "ok"


@app.route("/stats")
def stats():
    response = new_response()
    response.status = 200
    currentStats = programa.stats.get()

    response.set_data(dumps(currentStats).encode('utf-8'))
    return response


if __name__ == '__main__':
    app.run()
