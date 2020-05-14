#Niveau 3.3 exercice 4
"""Par 4T"""
def main():
   alphabet ={item : 0 for item in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
   texte = input().upper()
   for item in texte:
      for letter in alphabet:
         if letter == item:
            alphabet[letter] += 1
            break
   mostUse = "A"
   for lettre in alphabet:
      if alphabet[mostUse] < alphabet[lettre]:
         mostUse = lettre
   print(mostUse)
main()








"""Correction de France-ioi"""
texte = input()
nbOccurrences = [0] * 26
for idCaractere in range(len(texte)):
    caractereLu = texte[idCaractere]
    if caractereLu != " ":
        indiceLettre = ord(caractereLu.upper()) - ord("A")
        nbOccurrences[indiceLettre] = nbOccurrences[indiceLettre] + 1
indiceLettreMaxOcc = 0
for indiceLettre in range(26):
    if nbOccurrences[indiceLettre] > nbOccurrences[indiceLettreMaxOcc]:
        indiceLettreMaxOcc = indiceLettre

print(chr(indiceLettreMaxOcc + ord('A')))