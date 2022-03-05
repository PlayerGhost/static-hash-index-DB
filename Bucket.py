class Bucket:

    def __init__(self, stats, isOverflow):
        self.registros = []
        self.bucket = None
        self.stats = stats
        self.isOverflow = isOverflow

    def add(self, tupla):
        if len(self.registros) < 5:
            self.registros.append(tupla)
        else:
            if self.bucket is None:
                self.stats.addOverflow()
                self.bucket = Bucket(self.stats, True)
            self.bucket.add(tupla)

    def search(self, key):
        tupla = None

        for i in self.registros:
            if i[0] == key:
                tupla = i

                break

        if tupla is not None:
            return tupla
        else:
            if self.bucket is not None:
                return self.bucket.search(key)
            elif self.bucket is None:
                return None

    def countCollisions(self):
        if self.isOverflow:
            self.stats.addCollisions(len(self.registros))

        if self.bucket is not None:
            self.bucket.countCollisions()
