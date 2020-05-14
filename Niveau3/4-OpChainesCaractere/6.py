#Niveau 3.4 exercice 6
"""Par 4T"""
target = input().upper()
listeMot = input().upper().split(" ")
counter = 0
for Mot in listeMot:
   if Mot == target:
      counter += 1
print(counter)








"""Correction de France-ioi"""
motATrouver = input().upper()
mots = input().upper().split(" ")
nbFois = 0
for mot in mots:
   if mot == motATrouver:
      nbFois = nbFois + 1
print(nbFois)