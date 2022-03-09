from flask import Flask, request, Response
from json import dumps

from main import Programa

app = Flask(__name__)
programa = Programa()


def new_response(content=''):
    res = Response()
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.set_data(content.encode('utf8'))
    return res


@app.route("/")
def main():
    response = new_response()

    try:
        tamanhoPagina = int(request.args.get('pageSize'))
        programa.setup(tamanhoPagina)
        response.status = 200

    except ValueError:
        response.status = 500

    return response


if __name__ == '__main__':
    app.run()
