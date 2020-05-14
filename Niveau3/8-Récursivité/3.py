import sys
def triangle(debutX, milieuX, finX, debutY, milieuY, finY):
    if finX - debutX <= 1:
        yield debutX, debutY
    else:
        for x, y in triangle(debutX, int((milieuX+debutX) * 0.5), milieuX, debutY, int((milieuY+debutY) * 0.5), milieuY):
            yield x,y
        for x, y in triangle(milieuX, int(milieuX * 1.5 - debutX * 0.5), finX, debutY, int((milieuY+debutY) * 0.5), milieuY):
            yield x,y
        for x, y in triangle(debutX, int((milieuX+debutX) * 0.5), milieuX, milieuY, int(milieuY * 1.5 - debutY * 0.5), finY):
            yield x,y


nbrFois = int(input())
liste_return = []
for i in range(nbrFois):
    liste_return.append([" " for i2 in range(nbrFois-i)])

for x, y in triangle(0, int(nbrFois * 0.5), nbrFois, 0, int(nbrFois * 0.5), nbrFois):
    liste_return[y][x] = "#"

for ligne in range(nbrFois):
    for colonne in range(nbrFois-ligne):
        print(liste_return[ligne][colonne], end="")
    print()