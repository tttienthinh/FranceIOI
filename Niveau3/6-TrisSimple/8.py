from sys import stdin
liste_valeur = []

def find(valeur, borneinf, bornesup):
    global liste_valeur
    if bornesup - borneinf <= 1:
        return("0")

    new_borne = (borneinf + bornesup) // 2
    val_new_borne = liste_valeur[new_borne]

    if valeur == val_new_borne:
        return("1")
    elif valeur < val_new_borne:
        return(find(valeur, borneinf, new_borne))
    else:
        return(find(valeur, new_borne, bornesup))


def main():
    global liste_valeur
    nbr_valeur = int(input())
    liste_valeur = list(map(int, input().split()))
    nbr_demande = int(input())
    liste_valeur.sort()

    for i in range(nbr_demande):
        valeur = int(input())
        if valeur == liste_valeur[0] or valeur == liste_valeur[-1]:
            print("1\n")
        else:
            print(find(valeur, 0, nbr_valeur-1))

main()