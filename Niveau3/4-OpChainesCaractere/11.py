#Niveau 3.4 exercice 11
"""Par 4T"""
for page in range(2, int(input())+1):
   if page%2 == 0:
      decalage = -3*page
   else:
      decalage = 5*page
   for char in input():
      if char.isalpha():
         if char.islower():
            charNumber = (ord(char.upper())-65 + decalage) % 26
            char = chr(charNumber+65).lower()
         else:
            charNumber = (ord(char)-65 + decalage) % 26
            char = chr(charNumber+65)
      print(char, end="")
   print()








"""Correction de France-ioi"""
nbPages = int(input())
for idPage in range(2, nbPages+1):
   page = input()
   if idPage % 2 == 0:
      decalage = -3 * idPage
   else:
      decalage = 5 * idPage
   for idCaractere in range(len(page)):
      caractere = page[idCaractere]
      if caractere.isalpha():
         isMaj = caractere.isupper()
         if isMaj:
            caractere = caractere.lower()
         numero = (ord(caractere) - ord("a") + decalage) % 26
         caractere = chr(numero + ord("a"))
         if isMaj:
            caractere = caractere.upper()
      print(caractere, end = "")
   print()