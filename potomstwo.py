import copy
import math
from stan import Stan


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def potomstwo(stan, miasta):
    howMany = len(miasta)
    if len(stan.visited) >= howMany:
        print("Sth is no yes")
        return -1

    listaStanow = []

    for i in range(howMany):
        helper = Stan()
        helper.visited = copy.deepcopy(stan.visited)
        helper.currentCity = stan.currentCity
        helper.cost = stan.cost
        if i in helper.visited:
            continue
        else:
            helper.addCost(calculateDistance(miasta[stan.currentCity][1], miasta[stan.currentCity][2], miasta[i][1], miasta[i][2]))
            helper.addVisited(i)
            helper.setCurrentCity(i)
            listaStanow.append(helper)

    return listaStanow
