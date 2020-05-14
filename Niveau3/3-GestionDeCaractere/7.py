#Niveau 3.3 exercice 7
"""Par 4T"""
def main():
   score = [0]*26
   nbrLetter = 0
   texte = input().upper().replace(" ","")
   for caracter in texte:
      if caracter.isalpha():
         score[ord(caracter)-65] += 1
         nbrLetter += 1
   for item in score:
      print(item/nbrLetter)

main()








"""Correction de France-ioi"""
texte = input()
nbApparitions = [0] * 26
nbLettres = 0;
for posCaractere in range(len(texte)):
   caractere = texte[posCaractere];
   if caractere.isalpha():
      nbLettres = nbLettres + 1
      caractere = caractere.upper()
      num = ord(caractere) - ord("A")
      nbApparitions[num] = nbApparitions[num] + 1
for idLettre in range(26):
   print(nbApparitions[idLettre] / nbLettres)