#Niveau 3.6 exercice 2
"""Par 4T"""
def Aposer(bac, BacInitial):
   for initial in range(len(BacInitial)):
      if bac <= BacInitial[initial]:
         return(initial)
   return(len(BacInitial))


NbrBac = input().split(" ")
BacInitial = [int(i) for i in input().split()]
BacAPoser = [int(i) for i in input().split()]
ListeIndex = []
for bac in BacAPoser:
   BacIndex = Aposer(bac, BacInitial)
   ListeIndex.append(BacIndex)
   BacInitial.insert(BacIndex, bac)
print(" ".join([str(i) for i in ListeIndex]))
print(" ".join([str(i) for i in BacInitial]))









"""Correction de France-ioi"""
def main():
   nbBacsInitiaux, nbBacs = map(int, input().split())
   nbBacs += nbBacsInitiaux
   def lirePolluants():
      for polluant in input().split():
         yield polluant
      for polluant in input().split():
         yield polluant
   polluants = [int(polluant) for polluant in lirePolluants()]
   for position in range(nbBacsInitiaux, nbBacs):
      polluant = polluants[position]
      while position > 0 and (polluants[position - 1] >= polluant):
         polluants[position] = polluants[position - 1]
         position = position - 1
      polluants[position] = polluant
      print(position, end=" ")
   print()
   for polluant in polluants:
      print(polluant, end=" ")
   print()
main()