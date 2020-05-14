#Niveau 3.5 exercice 3
"""Par 4T"""
def main():
    def search(echequier):
        listCavalier = []
        for iLig in range(len(echequier)):
            for piece in range(len(echequier[iLig])):
                if echequier[iLig][piece] == "C":
                    listCavalier.append([iLig, piece])
        return (listCavalier)

    def aManger(listCavalier, echequier):
        for Cavalier in listCavalier:
            for deplacement in [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]:
                iLig = Cavalier[0] + deplacement[0]
                iCol = Cavalier[1] + deplacement[1]
                if iLig >= 0 and iLig <= 7 and iCol >= 0 and iCol <= 7:
                    if echequier[iLig][iCol].islower():
                        return (True)
        return (False)

    echequier = [list(input()) for i in range(8)]
    listCavalier = search(echequier)
    if aManger(listCavalier, echequier):
        print("yes")
    else:
        print("no")


main()








"""Correction de France-ioi"""
def main():
    echiquier = [input() for loop in range(8)]

    def piece(ligne, colonne):
        if (ligne < 0) or (ligne >= 8) or (colonne < 0) or (colonne >= 8):
            return ' '
        return echiquier[ligne][colonne]

    mouvements = [(+1, +2), (+1, -2), (-1, +2), (-1, -2), (+2, +1), (+2, -1), (-2, +1), (-2, -1)]

    def attaqueDeCavalier():
        for ligne in range(8):
            for colonne in range(8):
                if echiquier[ligne][colonne] == 'C':
                    for (deltaLigne, deltaColonne) in mouvements:
                        if piece(ligne + deltaLigne, colonne + deltaColonne).islower():
                            return True
        return False

    if attaqueDeCavalier():
        print("yes")
    else:
        print("no")


main()