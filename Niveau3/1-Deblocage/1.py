#Niveau 3 Deblocage exercice 1
"""Par 4T"""
liste = input().split(" ")
nbLivres = int(liste[0])
nbJours = int(liste[1])
dictionnaire = {}
for i in range(nbJours):
   nbClients = int(input())
   for loop in range(nbClients):
      emprunt = input().split(" ")
      if emprunt[0] in dictionnaire.keys():
         print(0)
      else:
         print(1)
         dictionnaire[emprunt[0]] = int(emprunt[1])
   eraserList = []
   for key in dictionnaire:
      dictionnaire[key] -= 1
      if dictionnaire[key] == 0:
         eraserList.append(key)
   for erase in eraserList:
      del dictionnaire[erase]








"""Correction de France-ioi"""
nbLivres, nbJours = map(int, input().split())
tempsRestantLivre = [0] * nbLivres
idLivre = 0
for loop in range(nbLivres):
    tempsRestantLivre[idLivre] = 0
    idLivre = idLivre + 1

for loop in range(nbJours):
    nbClients = int(input())
    for loop in range(nbClients):
        livre, temps = map(int, input().split())
        if (tempsRestantLivre[livre] <= 0):
            tempsRestantLivre[livre] = temps
            print(1)
        else:
            print(0)
    idLivre = 0
    for loop in range(nbLivres):
        tempsRestantLivre[idLivre] = tempsRestantLivre[idLivre] - 1
        idLivre = idLivre + 1