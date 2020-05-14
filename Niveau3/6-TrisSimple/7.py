#Niveau 3.6 exercice 7
"""Par 4T"""
from sys import stdin

nbr = int(stdin.readline())
Liste = [input() for i in range(nbr)]
Liste.sort()
print("\n".join(Liste))








"""Correction de France-ioi"""
def main():
   nbMots = int(input())
   mots = [input() for _ in range(nbMots)]
   mots.sort()
   for mot in mots:
      print(mot)
main()