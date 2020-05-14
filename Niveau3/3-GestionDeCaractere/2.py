#Niveau 3.3 exercice 2
"""Par 4T"""
def Num(nom):
   number = 0
   for item in nom:
      number += ord(item)-ord("A")
   while number >= 10:
      num = 0
      for item in str(number):
         num += int(item)
      number = num
   return(str(number))

nom = input().split(" ")
print(Num(nom[0])+" "+ Num(nom[1]))








"""Correction de France-ioi"""
prenoms = input().split(" ")
nombres = [0] * 2
for idPrenom in range(2):
   prenom = prenoms[idPrenom]
   nombre = 0
   for posLettre in range(len(prenom)):
      nombre = nombre + (ord(prenom[posLettre]) - ord("A"))
   while nombre >= 10:
      sommeChiffre = 0
      while nombre > 0:
         sommeChiffre = sommeChiffre + nombre % 10
         nombre = nombre // 10
      nombre = sommeChiffre
   nombres[idPrenom] = nombre
print("{} {}".format(nombres[0], nombres[1]))