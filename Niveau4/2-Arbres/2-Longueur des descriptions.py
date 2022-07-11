import sys

nbr_produit = int(input())
code_produit = [int(x) for x in input().split()]

if nbr_produit > 1000:
    sys.setrecursionlimit(nbr_produit+1)
# mémoïsation
longueur = [
    -1 for _ in range(nbr_produit+1)
]
longueur[0] = 0
def trouver_produit(recherche):
    if longueur[recherche] != -1:
        return longueur[recherche]
    else:
        res = trouver_produit(code_produit[recherche-1])+1
        longueur[recherche] = res
        return res


for recherche in range(1, nbr_produit+1):
    trouver_produit(recherche)

print(max(longueur))

# Proposition

"""
Bonjour,
J'ai codé en utilisant la mémoïsation.

Je reçois l'erreur "OutputTooBig", pouvez-vous m'aider à comprendre mon erreur s'il vous plaît.

"""

8
3 3 7 3 6 7 0 0

nbr_produit = 8
code_produit = [int(x) for x in "3 3 7 3 6 7 0 0".split()]

nbr_produit = int(input())
code_produit = [int(x) for x in input().split()]






indices = [-1 for _ in range(nbr_produit+1)]
indices[0] = 0
listes = [[]]

for i, x in enumerate(code_produit):
    if indices[x] == -1:
        indices[x] = len(listes)
        listes.append([i])
    else:
        listes[indices[x]].append(i)

def parcours(x):
    if indices[x] == -1:
        return 1
    else:
        liste = [parcours(y)+1 for y in listes[indices[x]]]
        return max(liste)

print(parcours(0))