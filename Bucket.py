class Bucket:

    def __init__(self, stats, isOverflow, bucketSize):
        self.registros = []
        self.bucket = None
        self.stats = stats
        self.isOverflow = isOverflow
        self.bucketSize = bucketSize

    def add(self, tupla):
        if len(self.registros) < self.bucketSize:
            self.registros.append(tupla)
            return

        if self.bucket is None:
            self.stats.addOverflow()
            self.bucket = Bucket(self.stats, True, self.bucketSize)

        self.bucket.add(tupla)

    def search(self, key):
        for i in self.registros:
            if i[0] == key:
                return i

        if self.bucket is not None:
            return self.bucket.search(key)

        return None

    def countCollisions(self):
        if self.isOverflow:
            self.stats.addCollisions(len(self.registros))

        if self.bucket is not None:
            self.bucket.countCollisions()
