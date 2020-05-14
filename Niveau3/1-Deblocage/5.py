#Niveau 3 Deblocage exercice 5
"""Par 4T"""
nbGrenouilles = int(input())
nbTours = int(input())
Grenouilles = {}  # dict ["nomGrenouille" : (distanceParcouru, nbTourEnTete)]
listTest = []
for nom in range(1, nbGrenouilles + 1):
    # initilization Grenouilles <dict> as distanceParcouru = 0 and nbTourEnTete = 0
    Grenouilles[nom] = [0, 0]

for i in range(nbTours):
    # increase nbTourEnTete for the best Grenouille
    entrée = input().split(" ")
    listTest.append(entrée)
    Grenouilles[int(entrée[0])][0] += int(entrée[1])
    if i != nbTours - 1:
        best = 0
        for grenouille in range(1, nbGrenouilles + 1):
            if Grenouilles[grenouille][0] > best:
                indexEnTete = grenouille
                best = Grenouilles[grenouille][0]
            elif Grenouilles[grenouille][0] == best:
                indexEnTete = 0
        if indexEnTete != 0:
            Grenouilles[indexEnTete][1] += 1

indexWinner = 1
for i in range(2, nbGrenouilles + 1):
    if Grenouilles[i][1] > Grenouilles[indexWinner][1]:
        indexWinner = i
print(indexWinner)








"""Correction de France-ioi"""
nbGrenouilles = int(input())
nbTours = int(input())
positions = [0] * (nbGrenouilles + 1)
nbToursEnTête = [0] * (nbGrenouilles + 1)
maximum = 0

for loop in range(nbTours - 1):
    grenouille, bond = map(int, input().split())
    positions[grenouille] = positions[grenouille] + bond
    if positions[grenouille] > maximum:
        nbToursEnTête[grenouille] = nbToursEnTête[grenouille] + 1
        maximum = positions[grenouille]
        grenouilleEnTête = grenouille
    elif positions[grenouille] == maximum:
        grenouilleEnTête = 0
    nbToursEnTête[grenouilleEnTête] = nbToursEnTête[grenouilleEnTête] + 1

nbToursEnTête[0] = 0
grenouilleGagnante = 1
nbToursGagnante = 0
for grenouille, nbTours in enumerate(nbToursEnTête):
    if nbToursGagnante < nbTours:
        nbToursGagnante = nbTours
        grenouilleGagnante = grenouille

print(grenouilleGagnante)