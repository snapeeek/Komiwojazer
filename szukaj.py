import random
import copy
import matplotlib.pyplot as plt
from stan import Stan
from potomstwo import potomstwo
from potomstwo import calculateDistance

iloscMiast = int(input("Podaj liczbe miast: "))
miasta = []
for i in range(iloscMiast):
    miasta.insert(i,  [i, random.randint(1, 40), random.randint(1,40)])

# miasta = [[0, 9, 11], [1, 18, 9], [2, 21, 14], [3, 4, 17], [4, 5, 3]]

aktualnyStan = Stan()
i = random.randrange(0, iloscMiast)
aktualnyStan.setCurrentCity(i)
aktualnyStan.addVisited(i)
stany = potomstwo(aktualnyStan, miasta)
helper = []
print("Miasto poczatkowe: ", i)

while len(stany[0].visited) != iloscMiast:
    helper = []
    for i in stany:
        temp = potomstwo(i, miasta)
        for j in temp:
            helper.append(j)
    stany = helper

for i in stany:
    i.addVisited(i.visited[0])
    i.addCost(calculateDistance(miasta[i.currentCity][1],miasta[i.currentCity][2],miasta[i.visited[0]][1],miasta[i.visited[0]][2]))


stany.sort()

for i in stany:
    print(i.visited)
    print(i.cost)

print(stany[0].cost)
x = []
y = []
for i in stany[0].visited:
    x.append(miasta[i][1])
    y.append(miasta[i][2])

x.append(miasta[stany[0].visited[0]][1])
y.append(miasta[stany[0].visited[0]][2])
plt.plot(x, y)
print(miasta)
print(stany[0].visited)
for i in range(len(x)-1):
    label=stany[0].visited[i]
    plt.annotate(label,  # this is the text
                 (x[i], y[i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

plt.show()