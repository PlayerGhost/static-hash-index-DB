class Stats:

    def __init__(self):
        self.colisoes = 0
        self.overflows = 0

    def addColision(self):
        self.colisoes += 1

    def addOverflow(self):
        self.overflows += 1
