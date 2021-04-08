from os import sys


nbr_produit = int(input())
code_produit = [int(item) for item in input().split()]
plus_long = 0
arbre = {}

def trouver_produit(recherche, longueur=0):
    global recherches, arbre

    deja_trouve = True
    try:
        longueur_trouve = trouve[recherche]
    except:
        deja_trouve = False

    if recherche == 0:
        return longueur
    elif deja_trouve:
        return longueur + longueur_trouve
    else:
        nouvelle_longueur = trouver_produit(code_produit[recherche - 1], longueur+1)
        trouve[recherche] = nouvelle_longueur - longueur
        return nouvelle_longueur


sys.setrecursionlimit(len(code_produit))
for recherche in range(1, nbr_produit+1):
    nouvelle_longueur = trouver_produit(recherche)
    if nouvelle_longueur > plus_long:
        plus_long = nouvelle_longueur

print(plus_long)
