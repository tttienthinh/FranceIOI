#Niveau 3.5 exercicie 1
"""Par 4T"""
tableauTaille =input().split(" ")
tableau = [["."]*int(tableauTaille[1]) for i in range(int(tableauTaille[0]))]
#Tableau = [Colonnes[Lignes]]
for i in range(int(input())):
   Bords = input().split(" ")
   motif = Bords[4]
   for iLig in range(int(Bords[0]), int(Bords[2])+1):
      for iCol in range(int(Bords[1]), int(Bords[3])+1):
         tableau[iLig][iCol] = motif
for i in range(len(tableau)):
   print("".join(tableau[i]))








"""Correction de France-ioi"""
def main():
   nbLignes, nbColonnes = map(int, input().split())
   image = [["."] * nbColonnes for _ in range(nbLignes)]
   nbRectangles = int(input())
   for iRectangle in range(nbRectangles):
      donnéesRect = input().split()
      iLig1, iCol1, iLig2, iCol2 = map(int, donnéesRect[:4])
      couleur = donnéesRect[4]
      for  iLig in range(iLig1, iLig2 + 1):
         for iCol in range(iCol1, iCol2 + 1):
            image[iLig][iCol] = couleur
   for ligne in image:
      print("".join(ligne))
main()