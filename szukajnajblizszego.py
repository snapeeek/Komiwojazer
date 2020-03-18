import random
import copy
import matplotlib.pyplot as plt
from stan import Stan
from potomstwo import potomstwo

iloscMiast = int(input("Podaj liczbe miast: "))
miasta = []
for i in range(iloscMiast):
    miasta.insert(i,  [i, random.randint(1, 40), random.randint(1,40)])

# miasta = [[0, 9, 11], [1, 18, 9], [2, 21, 14], [3, 4, 17], [4, 5, 3]]

aktualnyStan = Stan()
i = random.randrange(0, iloscMiast)
aktualnyStan.setCurrentCity(i)
aktualnyStan.addVisited(i)
stany = aktualnyStan

print(i)

for i in range(iloscMiast - 1):
    temp = potomstwo(stany, miasta)
    temp.sort()
    stany = temp[0]

print(stany.cost)

x = []
y = []
for i in stany.visited:
    x.append(miasta[i][1])
    y.append(miasta[i][2])

x.append(miasta[stany.visited[0]][1])
y.append(miasta[stany.visited[0]][2])
plt.plot(x, y)
print(miasta)
print(stany.visited)
for i in range(len(x)-1):
    label=stany.visited[i]
    plt.annotate(label,  # this is the text
                 (x[i], y[i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

plt.show()