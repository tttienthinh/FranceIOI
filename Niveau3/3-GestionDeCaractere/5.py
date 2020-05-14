#Niveau 3.3 exercice 5
"""Par 4T"""
def Palindrome(texte):
   answer = True
   for i in range(len(texte)):
      if texte[i] != texte[-i-1]:
         answer = False
         return(answer)
   return(answer)



def main():
   for nbrText in range(int(input())):
      texte = input()
      if Palindrome(texte.upper().replace(" ","")):
         print(texte)

main()








"""Correction de France-ioi"""
nbLivres = int(input())
for loop in range(nbLivres):
   titre = input()
   titreMaj = titre.upper()
   estPalindrome = True
   debut = 0
   fin = len(titreMaj) - 1
   while (debut < fin):
      if titreMaj[debut] == ' ':
         debut = debut + 1
      elif titreMaj[fin] == ' ':
         fin = fin - 1
      else:
         if titreMaj[debut] != titreMaj[fin]:
            estPalindrome = False
         debut = debut + 1
         fin = fin - 1
   if estPalindrome:
      print(titre)