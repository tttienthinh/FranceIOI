nbr_produit = int(input())
code_produit = input().split()
nbr_recherche = int(input())
recherches = input().split()


def trouver_produit(recherche):
    global recherches
    if recherche == "0":
        return
    else:
        trouver_produit(code_produit[int(recherche) - 1])
        if code_produit[int(recherche) - 1] != "0":
            print(code_produit[int(recherche) - 1], end=" ")


for recherche in recherches:
    trouver_produit(recherche)
    print(recherche)
