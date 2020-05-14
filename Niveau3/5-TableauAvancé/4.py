#Niveau 3.4 exercice 4
"""Par 4T"""
def Gagner(plateau, N, joueur):
    for iLig in range(N):
        counter = 0
        for iCol in range(N):
            if plateau[iLig][iCol] == joueur:
                counter += 1
                if counter == 5:
                    return (True)
            else:
                counter = 0

    for iCol in range(N):
        counter = 0
        for iLig in range(N):
            if plateau[iLig][iCol] == joueur:
                counter += 1
                if counter == 5:
                    return (True)
            else:
                counter = 0

    for Diag1 in range(4, N):
        counter1 = 0
        counter2 = 0
        for position in range(Diag1 + 1):
            if plateau[Diag1 - position][position] == joueur:
                counter1 += 1
                if counter1 == 5:
                    return (True)
            else:
                counter1 = 0
            if plateau[(N - 1) - Diag1 + position][(N - 1) - position] == joueur:
                counter2 += 1
                if counter2 == 5:
                    return (True)
            else:
                counter2 = 0

    for Diag2 in range(N - 4):
        counter1 = 0
        counter2 = 0
        for position in range(Diag2, N):
            if plateau[position - Diag2][position] == joueur:
                counter1 += 1
                if counter1 == 5:
                    return (True)
            else:
                counter1 = 0
            if plateau[position][position - Diag2] == joueur:
                counter2 += 1
                if counter2 == 5:
                    return (True)
            else:
                counter2 = 0

    return (False)


N = int(input())
plateau = [input().split(" ") for i in range(N)]
if Gagner(plateau, N, "1"):
    print("1")
elif Gagner(plateau, N, "2"):
    print("2")
else:
    print("0")








"""Correction de France-ioi"""
def main():
    taille = int(input())
    plateau = [list(map(int, input().split())) for loop in range(taille)]

    def pion(ligne, colonne):
        nonlocal taille
        if (ligne < 0) or (taille <= ligne) or (colonne < 0) or (taille <= colonne):
            return 0
        else:
            return plateau[ligne][colonne]

    deltaLig = [-1, 0, 1, 1]
    deltaCol = [1, 1, 1, 0]

    for ligne in range(taille):
        for colonne in range(taille):
            joueur = plateau[ligne][colonne]
            if joueur > 0:
                for direction in range(4):
                    lig = ligne
                    col = colonne
                    alignés = 1
                    for loop in range(4):
                        lig += deltaLig[direction]
                        col += deltaCol[direction]
                        if pion(lig, col) == joueur:
                            alignés += 1
                    if alignés == 5:
                        print(joueur)
                        exit(0)
    print(0)


main()