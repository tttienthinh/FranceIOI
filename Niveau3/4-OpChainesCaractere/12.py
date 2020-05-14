#Niveau 3.4 exercice 12
"""Par 4T"""
phrase = list(input())
counter = [0]*26
for char in phrase:
   if char.isalpha():
      counter[ord(char.upper())-65] += 1
mostUsed = 0
for char in range(1,len(counter)):
   if counter[char] > counter[mostUsed]:
      mostUsed = char
decalage = 4 - mostUsed
for char in phrase:
   if char.isalpha():
      if char.islower():
         charNumber = (ord(char.upper())-65 + decalage) % 26
         char = chr(charNumber+65).lower()
      else:
         charNumber = (ord(char)-65 + decalage) % 26
         char = chr(charNumber+65)
   print(char, end="")








"""Correction de France-ioi"""
texte = input()
# Trouver la lettre la plus frequente
nbOccurrences = [0] * 26
for idCaractere in range(len(texte)):
    caractereLu = texte[idCaractere]
    if caractereLu.isalpha():
        indiceLettre = ord(caractereLu.upper()) - ord("A")
        nbOccurrences[indiceLettre] = nbOccurrences[indiceLettre] + 1
indiceLettreMaxOcc = 0
for indiceLettre in range(26):
    if nbOccurrences[indiceLettre] > nbOccurrences[indiceLettreMaxOcc]:
        indiceLettreMaxOcc = indiceLettre

# On connait le decalage !
decalage = -(indiceLettreMaxOcc - (ord("E") - ord("A")))
# Decodage
for idCaractere in range(len(texte)):
    caractere = texte[idCaractere]
    if caractere.isalpha():
        isMaj = caractere.isupper()
        if isMaj:
            caractere = caractere.lower()
        numero = (ord(caractere) - ord("a") + decalage) % 26
        caractere = chr(numero + ord("a"))
        if isMaj:
            caractere = caractere.upper()
    print(caractere, end="")
print()