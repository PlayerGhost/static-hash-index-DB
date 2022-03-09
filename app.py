from flask import Flask, request

from main import Programa

app = Flask(__name__)
programa = Programa()


@app.route("/")
def main():
    tamanhoPagina = int(request.args.get('pageSize'))
    programa.setup(tamanhoPagina)
    print(programa.numeroBuckets)
    return 'teste'


if __name__ == '__main__':
    app.run()
