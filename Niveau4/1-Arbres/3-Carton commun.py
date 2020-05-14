from os import sys

nbr_produit = int(input())
code_produit = [int(item) for item in input().split()]
nbr_recherche = int(input())
recherches = [[int(item) for item in input().split()] for _ in range(nbr_recherche)]
arbre = {}

def trouver_chemin(produit, chemin=[]):
    global code_produit, arbre

    deja_trouve = True
    try:
        chemin_trouve = arbre[produit]
    except:
        deja_trouve = False

    if produit == 0:
        return [0] + chemin
    elif deja_trouve:
        return chemin_trouve[:-1] + [produit] + chemin
    else:
        nouveau_chemin = trouver_chemin(code_produit[produit - 1], [produit]+chemin)
        arbre[produit] = nouveau_chemin[:-(len(chemin)+1)] + [produit]
        return nouveau_chemin


def trouver_commun(index_min, index_max, petit_produit, grand_produit):
    global arbre
    index_moy = int((index_min+index_max)/2)
    if (index_max - index_min) <= 1:
        if arbre[petit_produit][index_max] == arbre[grand_produit][index_max]:
            return arbre[petit_produit][index_max]
        else:
            return arbre[petit_produit][index_min]
    elif arbre[petit_produit][index_moy] == arbre[grand_produit][index_moy]:
        return trouver_commun(index_moy, index_max, petit_produit, grand_produit)
    else:
        return trouver_commun(index_min, index_moy, petit_produit, grand_produit)

def trouver_trop_long(produit):
    global code_produit
    if produit == 0:
        yield produit
    else:
        yield produit
        for item in trouver_trop_long(code_produit[produit-1]):
            yield item

sys.setrecursionlimit(20000)
if len(code_produit) > 15000 or True:
    for recherche in recherches:
        liste_un = [_ for _ in trouver_trop_long(recherche[0])]
        for item in trouver_trop_long(recherche[0]):
            if item in liste_un:
                print(item)
                break
"""else:
    for produit in range(1, nbr_produit+1):
        trouver_chemin(produit)

    for recherche in recherches:
        if len(arbre[recherche[0]]) < len(arbre[recherche[1]]):
            print(trouver_commun(0, len(arbre[recherche[0]])-1, recherche[0], recherche[1]))
        else:
            print(trouver_commun(0, len(arbre[recherche[1]])-1, recherche[1], recherche[0]))"""
