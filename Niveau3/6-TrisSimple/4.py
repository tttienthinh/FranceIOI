#Niveau 3.6 exercice 4
"""Par 4T"""
from sys import stdin

stdin.readline()
ListeBac = [int(bac) for bac in stdin.readline().split()]
ListeBac.sort()
print(" ".join([str(bac) for bac in ListeBac]))








"""Correction de France-ioi"""
import sys

valeurs = []
def indexDuMaximum(nbRestant):
    indexDuMax = 0
    for index in range(nbRestant):
        if valeurs[index] > valeurs[indexDuMax]:
            indexDuMax = index
    return indexDuMax


def triSelection():
    global valeurs
    for nbRestant in range(len(valeurs), 0, -1):
        indiceMax = indexDuMaximum(nbRestant)
        valeurs[indiceMax], valeurs[nbRestant - 1] = valeurs[nbRestant - 1], valeurs[indiceMax]


def main():
    global valeurs
    _ = int(input())
    valeurs = list(map(int, sys.stdin.readline().split()))

    triSelection()

    for valeur in valeurs:
        print(valeur, end=" ")


main()