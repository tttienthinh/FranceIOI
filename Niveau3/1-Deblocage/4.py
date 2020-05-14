#Niveau 3 Deblocage exercice 4
"""Par 4T"""
nbMesures = int(input())
diffMax = float(input())
Mesures = []
for i in range(nbMesures):
    Mesures.append(float(input()))


def nbPassage(nbMesures, diffMax, Mesures):
    Passage = 0
    while True:
        okay = 1
        for i in range(1, nbMesures):
            if abs(Mesures[i] - Mesures[i - 1]) >= diffMax:
                okay = 0
                break
        if okay == 1:
            return (Passage)
        newMesures = [Mesures[0]]
        for i in range(1, nbMesures - 1):
            newMesures.append((Mesures[i - 1] + Mesures[i + 1]) / 2)
        newMesures.append(Mesures[nbMesures - 1])
        Passage += 1
        Mesures = newMesures


print(nbPassage(nbMesures, diffMax, Mesures))







"""Correction de France-ioi"""
nbValeurs = int(input())
seuil = float(input())
valeurs = [float(input()) for loop in range(nbValeurs)]
temp = [0.0] * nbValeurs


def lisse():
    for valeur in range(1, nbValeurs):
        if abs(valeurs[valeur] - valeurs[valeur - 1]) > seuil:
            return False
    return True


nbTours = 0
while not lisse():
    nbTours = nbTours + 1
    for valeur in range(1, nbValeurs - 1):
        temp[valeur] = (valeurs[valeur - 1] + valeurs[valeur + 1]) / 2
    for valeur in range(1, nbValeurs - 1):
        valeurs[valeur] = temp[valeur]

print(nbTours)