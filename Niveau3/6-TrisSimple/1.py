#Niveau 3.6 exercice 1
"""Par 4T"""
NbrBac = input().split(" ")
BacPolluant = [int(i) for i in input().split()]
BacPolluant.sort()
print(" ".join([str(BacPolluant[int(NbrBac[0])-i]) for i in range(1, int(NbrBac[1])+1)]))








"""Correction de France-ioi"""
import sys

nbValeurs = 0
valeurs = []


def indexDuMaximum():
    indexDuMax = 0
    for pos in range(nbValeurs):
        if valeurs[pos] > valeurs[indexDuMax]:
            indexDuMax = pos
    return indexDuMax


def extraitMaximum():
    global nbValeurs, valeurs
    indexDuMax = indexDuMaximum()
    value = valeurs[indexDuMax]
    valeurs[indexDuMax] = valeurs[nbValeurs - 1]
    nbValeurs -= 1
    return value


def main():
    global nbValeurs, valeurs
    nbValeurs, nbExtractions = map(int, input().split())
    valeurs = list(map(int, sys.stdin.readline().split()))
    print(" ".join(map(str, [extraitMaximum() for _ in range(nbExtractions)])))


main()