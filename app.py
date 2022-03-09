from flask import Flask, request

from main import Programa

app = Flask(__name__)
programa = Programa()

@app.route("/")
def main():
    tamanhoPagina = int(request.args.get('pageSize')) # páginas vazias (??)
    programa.setup(tamanhoPagina)
    return '{} -> {}'.format(programa.numeroBuckets, programa.buckets)


app.run()