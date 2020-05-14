#Niveau 3.4 exercice 10
"""Par 4T"""
decrypte = list(input())
Mot = input()
for char in Mot:
   if char.isalpha():
      if char.islower():
         print(decrypte[ord(char.upper())-65], end="")
      else:
         print(decrypte[ord(char)-65].upper(), end="")
   else:
      print(char, end="")








"""Correction de France-ioi"""
decrypteur = input()
texte = input()
caractere = 0
for loop in range(len(texte)):
   caractereLu = texte[caractere]
   if caractereLu.isalpha():
      if caractereLu.isupper():
         caractereLu = decrypteur[ord(caractereLu.lower()) - ord("a")].upper()
      else:
         caractereLu = decrypteur[ord(caractereLu) - ord("a")]
   print(caractereLu, end = '')
   caractere = caractere + 1