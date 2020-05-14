#Niveau 3.4 exercice 3
"""Par 4T"""
def Verification(ordre):
    sortedOrdre = ordre.copy()
    sortedOrdre.sort()
    if ordre == sortedOrdre:
        return (True)
    else:
        return (False)


def main():
    titres = [input() for i in range(int(input()))]
    lu = titres[0]
    for livre in titres:
        if Verification([lu, livre]):
            print(livre)
            lu = livre


main()








"""Correction de France-ioi"""
nbLivres = int(input())
plusGrandTitre = ""
for loop in range(nbLivres):
   titreLivre = input()
   if titreLivre > plusGrandTitre:
      plusGrandTitre = titreLivre
      print(titreLivre)