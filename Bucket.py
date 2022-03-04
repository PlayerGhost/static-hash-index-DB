class Bucket:

    def __init__(self):
        self.registros = []
        self.bucket = None

    def add(self, tupla):

        if len(self.registros) < 5:
            self.registros.append(tupla)
        else:
            if self.bucket is None:
                self.bucket = Bucket()
            self.bucket.add(tupla)
