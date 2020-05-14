#Niveau 3.4 exercice 1
"""Par 4T"""
def main():
   livres = [input() for i in range(int(input()))]
   for nom in list(reversed(livres)):
      print(nom)

main()








"""Correction de France-ioi"""
nbLivres = int(input())
titres = [" "] * nbLivres
for idLivre in range(nbLivres):
   titres[idLivre] = input()
for idLivre in range(nbLivres):
   print(titres[nbLivres - 1 - idLivre])