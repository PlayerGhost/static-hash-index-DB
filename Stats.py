class Stats:
    def __init__(self):
        self.reset()

    def reset(self):
        self.custo = 0
        self.overflows = 0
        self.collisions = 0

    def addCollisions(self, collisions):
        self.collisions += collisions

    def addOverflow(self):
        self.overflows += 1

    def addCusto(self):
        self.custo += 1

    def get(self):
        return {
            'collisions': self.collisions,
            'overflows': self.overflows,
            'custo': self.custo
        }
