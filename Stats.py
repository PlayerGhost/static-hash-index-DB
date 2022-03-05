class Stats:

    def __init__(self):
        self.colisoes = 0
        self.overflows = 0
        self.custo = 0

    def addCollisions(self, collisions):
        self.colisoes += collisions

    def addOverflow(self):
        self.overflows += 1

    def setCusto(self, custo):
        self.custo = custo
