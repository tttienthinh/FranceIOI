from sys import stdin
def Counter(liste_caractere):
    gauche, droite = 0, 0
    for i in liste_caractere:
        if i == "(":
            gauche += 1
        elif i == ")":
            droite += 1
    if gauche == droite:
        return(True)
    else:
        return(False)

def Deleter(liste_caractere):
    while True:
        indexMax = len(liste_caractere)-1
        for i in range(indexMax):
            if liste_caractere[i] == "(" and liste_caractere[i+1] == ")":
                toDelete = [i,i+1]
                break
            if i == indexMax-1:
                return(False)
        del liste_caractere[toDelete[0]]
        del liste_caractere[toDelete[0]]
        if len(liste_caractere) == 0:
            return(True)

def main():
    nbr_caractere = int(stdin.readline()[:-1])
    liste_caractere = [caractere for caractere in list(stdin.readline()[:-1]) if caractere != " "]
    reponse = "0"
    if Counter(liste_caractere):
        if Deleter(liste_caractere):
            reponse ="1"
    print(reponse)
main()




"""correction"""


def main():
    _ = int(input())
    plan = input()
    niveau = 0
    for caractere in plan:
        if caractere == "(":
            niveau = niveau + 1
        elif caractere == ")":
            niveau = niveau - 1
            if niveau < 0:
                print(0)
                return

    if niveau == 0:
        print(1)
    else:
        print(0)


main()