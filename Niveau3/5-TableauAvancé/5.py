#Niveau 3.5 exercice 5
"""Par 4T"""
NbrErodage = int(input())
tailleGrille = input().split()
grille = []
newGrille = []
for i in range(int(tailleGrille[0])):
   grille.append(list(input()))

newGrille = [liste.copy() for liste in grille]
for i in range(NbrErodage):
   for iLig in range(int(tailleGrille[0])):
      for iCol in range(int(tailleGrille[1])):
         if iLig != 0 and iLig != int(tailleGrille[0])-1 and iCol != 0 and iCol != int(tailleGrille[1])-1:
            if grille[iLig][iCol] == "#":
               if grille[iLig+1][iCol] == "#" and grille[iLig-1][iCol] == "#" and grille[iLig][iCol+1] == "#" and grille[iLig][iCol-1] == "#" :
                  newGrille[iLig][iCol] = "#"
               else:
                  newGrille[iLig][iCol] = "."
            else:
               newGrille[iLig][iCol] = "."
         else:
            newGrille[iLig][iCol] = "."
   grille = [liste.copy() for liste in newGrille]

for i in range(int(tailleGrille[0])):
   print("".join(grille[i]))








"""Correction de France-ioi"""
import sys


def main():
    nbPassages = int(sys.stdin.readline())
    nbLignes, nbColonnes = map(int, sys.stdin.readline().split())
    grille = [list('.' + sys.stdin.readline().strip() + '.') for loop in range(nbLignes)]
    bord = ['.'] * (nbColonnes + 2)
    grille = [bord] + grille + [bord]

    def frontiere():
        nonlocal nbLignes
        nonlocal nbColonnes
        maxLignes = nbLignes + 1
        maxColonnes = nbColonnes + 1
        for ligne in range(1, maxLignes):
            for colonne in range(1, maxColonnes):
                if grille[ligne][colonne] == '#' and \
                        ((grille[ligne - 1][colonne] == '.') or \
                                 (grille[ligne + 1][colonne] == '.') or \
                                 (grille[ligne][colonne - 1] == '.') or \
                                 (grille[ligne][colonne + 1] == '.')):
                    yield (ligne, colonne)

    nouveauxPoints = list(frontiere())
    for (ligne, colonne) in nouveauxPoints:
        grille[ligne][colonne] = '.'

    def nouvelleFrontiere():
        for (ligne, colonne) in nouveauxPoints:
            if grille[ligne - 1][colonne] == '#':
                grille[ligne - 1][colonne] = '.'
                yield (ligne - 1, colonne)
            if grille[ligne + 1][colonne] == '#':
                grille[ligne + 1][colonne] = '.'
                yield (ligne + 1, colonne)
            if grille[ligne][colonne - 1] == '#':
                grille[ligne][colonne - 1] = '.'
                yield (ligne, colonne - 1)
            if grille[ligne][colonne + 1] == '#':
                grille[ligne][colonne + 1] = '.'
                yield (ligne, colonne + 1)

    for loop in range(1, nbPassages):
        nouveauxPoints = list(nouvelleFrontiere()

    for ligne in grille[1:-1]:
        print("".join(ligne[1:-1]))


main()