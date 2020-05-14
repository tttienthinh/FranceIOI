#Niveau 3.4 exercice 7
"""Par 4T"""
acronyme = input()
titre = []
for i in range(int(input())):
   titre.append(input().upper().split(" "))
for i in range(len(titre)):
   Okay = True
   if len(acronyme) == len(titre[i]):
      for loop in range(len(acronyme)):
         if titre[i][loop][0] != acronyme[loop]:
            Okay = False
      if Okay:
         printer = []
         for i in titre[i]:
            printer.append(i.capitalize())
         print(" ".join(printer))








"""Correction de France-ioi"""
acronyme = input()
nbMots = len(acronyme)
nbLivres = int(input())
for _ in range(nbLivres):
   titre = [mot.capitalize() for mot in input().split()]
   if len(titre) == nbMots:
      correspondance = True
      for mot,initiale in zip(titre,acronyme):
         correspondance = correspondance and (initiale == mot[0])
      if correspondance:
         print(" ".join(titre))