#Niveau 3.5 exercice 2
"""Par 4T"""
def isMagic(liste, N):
    somme = sum(liste[0])
    AlreadyUsed = []
    for Ligne in liste:
        if sum(Ligne) != somme:
            return (False)
        for nbr in Ligne:
            if nbr in AlreadyUsed:
                return (False)
            AlreadyUsed.append(nbr)
    AlreadyUsed.sort()
    if AlreadyUsed != [i for i in range(1, N ** 2 + 1)]:
        return (False)
    for NbrCol in range(N):
        Colonne = [Ligne[NbrCol] for Ligne in liste]
        if sum(Colonne) != somme:
            return (False)
    sommeDiag1 = 0
    sommeDiag2 = 0
    for iDiag in range(N):
        sommeDiag1 += liste[iDiag][iDiag]
        sommeDiag2 += liste[N - 1 - iDiag][iDiag]
    if sommeDiag1 != somme:
        return (False)
    if sommeDiag2 != somme:
        return (False)
    return (True)


N = int(input())
carreMagic = [[0] * N for i in range(N)]
for iLig in range(N):
    Nbr = input().split(" ")
    for iCol in range(N):
        carreMagic[iLig][iCol] = int(Nbr[iCol])
if isMagic(carreMagic, N):
    print("yes")
else:
    print("no")








"""Correction de France-ioi"""
def main():
    def tousNombresPresents():
        nonlocal tailleGrille
        maxVal = tailleGrille * tailleGrille + 1
        presents = [False] * maxVal
        for ligne in nombresCarre:
            for nombre in ligne:
                if (nombre <= 0) or (nombre >= maxVal) or presents[nombre]:
                    return False
                else:
                    presents[nombre] = True
        return True

    def totauxCorrects():
        nonlocal tailleGrille

        def totalPourDirection(linDepart, colDepart, deltaLin, deltaCol):
            nonlocal tailleGrille
            lin, col = linDepart, colDepart
            total = 0
            for loop in range(tailleGrille):
                total += nombresCarre[lin][col]
                lin += deltaLin
                col += deltaCol
            return total

        total = totalPourDirection(0, 0, 1, 1)
        if (totalPourDirection(0, tailleGrille - 1, 1, -1) != total):
            return False
        for position in range(tailleGrille):
            if totalPourDirection(position, 0, 0, 1) != total:
                return False
            if totalPourDirection(0, position, 1, 0) != total:
                return False
        return True

    tailleGrille = int(input())
    nombresCarre = [list(map(int, input().split())) for loop in range(tailleGrille)]
    if tousNombresPresents() and totauxCorrects():
        print("yes")
    else:
        print("no")


main()