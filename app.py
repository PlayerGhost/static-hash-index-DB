from flask import Flask, request, Response
from json import dumps

from main import Programa

app = Flask(__name__)
programa = Programa()


def new_response():
    res = Response()
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route("/")
def main():
    response = new_response()

    try:
        tamanhoPagina = int(request.args.get('pageSize', None))
        programa.setup(tamanhoPagina)
        response.status = 200

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

        programa.stats.reset()
        result = programa.searchOnBucket(palavra)
        content = {
            'result': result,
            'stats': programa.stats.get()
        }
        response.set_data(dumps(content).encode('utf8'))


    except ValueError:
        response.status = 500
    
    return response


if __name__ == '__main__':
    app.run()
