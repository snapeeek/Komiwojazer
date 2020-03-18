class Stan:
    currentCity = -1
    visited = []
    cost = 0

    def setCurrentCity(self, miasto):
        self.currentCity = miasto

    def addVisited(self, miasto):
        self.visited.append(miasto)

    def addCost(self, c):
        self.cost = self.cost + c

    def __lt__(self, other):
        return self.cost < other.cost
