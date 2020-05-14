#Niveau 3.6 exercice 3
"""Par 4T"""
input()
Automobiles = []
for car in input().split(" "):
   try:
      Automobiles.append(int(car))
   except:
      i = 0
Comparaison = Automobiles.copy()
Comparaison.sort()
depassement = []
while Comparaison != Automobiles:
   for i in range(len(Automobiles)-1):
      if Automobiles[i] > Automobiles[i+1]:
         Automobiles[i], Automobiles[i+1] = Automobiles[i+1], Automobiles[i]
         depassement.append(str(Automobiles[i+1])+" "+str(Automobiles[i]))

print(len(depassement))
print("\n".join(depassement))







"""Correction de France-ioi"""
import sys


def main():
    nbAutos = int(input())
    idAuto = list(map(int, sys.stdin.readline().split()))

    depassementsEffectues = []
    for _ in range(nbAutos):
        for rang in range(nbAutos - 1):
            if idAuto[rang] > idAuto[rang + 1]:
                depassementsEffectues.append((idAuto[rang], idAuto[rang + 1]))
                idAuto[rang], idAuto[rang + 1] = idAuto[rang + 1], idAuto[rang]

    sys.stdout.write(str(len(depassementsEffectues)) + "\n")
    for (idAutoDepassee, idAutoQuiDepasse) in depassementsEffectues:
        sys.stdout.write(str(idAutoDepassee) + " " + str(idAutoQuiDepasse) + "\n")


main()