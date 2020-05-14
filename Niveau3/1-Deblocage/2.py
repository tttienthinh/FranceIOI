#Niveau 3 Deblocage exercice 2
"""Par 4T"""
nbLettres = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(nbLettres*2-1):
   if i>=nbLettres:
      num = (nbLettres*2-1)-(i+1)
   else:
      num = i
   char = alphabet[num]* ((nbLettres*2-1) - num*2)
   for loop in range(1,num+1):
      char = alphabet[num-loop]+char+alphabet[num-loop]
   print(char)








"""Correction de France-ioi"""
nbLettres = int(input())
lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
taille = 2*nbLettres - 1
iLig = 0
for loop in range(taille):
   iCol = 0
   for loop in range(taille):
      print(lettre[min(min(iLig,taille-1-iLig), min(iCol, taille-1-iCol))], end = "")
      iCol = iCol + 1
   iLig = iLig + 1
   print("")