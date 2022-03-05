class Stats:

    def __init__(self):
        self.collisions = 0
        self.overflows = 0
        self.custo = 0

    def addCollisions(self, collisions):
        self.collisions += collisions

    def addOverflow(self):
        self.overflows += 1

    def addCusto(self):
        self.custo += 1
