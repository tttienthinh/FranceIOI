#Niveau 3.6 exercice 5
"""Par 4T"""
from sys import stdin

stdin.readline()
ListeBac = [int(bac) for bac in stdin.readline().split()]
ListeBac.sort()
print(" ".join([str(bac) for bac in ListeBac]))







"""Correction de France-ioi"""import sys
def main():
   nbValeurs = int(input())
   valeurs = list(map(int, sys.stdin.readline().split()))
   valeurs.sort()

   for valeur in valeurs:
      print(valeur, end = " ")
main()