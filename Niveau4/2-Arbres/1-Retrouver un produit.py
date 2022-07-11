

nbr_produit = int(input())
code_produit = [int(x) for x in input().split()]
nbr_recherche = int(input())
recherches = [int(x) for x in input().split()]


def trouver_produit(recherche):
    if recherche == 0:
        return []
    else:
        return trouver_produit(code_produit[recherche-1])+[str(recherche)]


for recherche in recherches:
    print(" ".join(trouver_produit(recherche)))


