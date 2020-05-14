#Niveau 3.4 exercice 2
"""Par 4T"""
def main():
   bibliotheque = [input() for i in range(int(input()))]
   bibliotheque.sort()
   for livre in bibliotheque:
      print(livre)
main()








"""Correction de France-ioi"""
nbLivres = int(input())
titres = [" "] * nbLivres
for idLivre in range(nbLivres):
   titres[idLivre] = input()
titres.sort()
for idLivre in range(nbLivres):
   print(titres[idLivre])