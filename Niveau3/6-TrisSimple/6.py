#Niveau 3.6 exercice 6
"""Par 4T"""
from sys import stdin

nbBacs = int(stdin.readline())
Liste = []
for i in range(nbBacs):
   Bac = stdin.readline().split()
   Liste.append([int(Bac[1]), int(Bac[0])])
Liste.sort()
for i in Liste:
   print(str(i[1])+" "+str(i[0]))







"""Correction de France-ioi"""
import sys
def main():
   nbBacs = int(input())
   bacs = [list(map(int, sys.stdin.readline().split())) for _ in range(nbBacs)]
   bacs.sort(key = lambda bac: (bac[1], bac[0]))
   for bac in bacs:
      print(*bac)
main()