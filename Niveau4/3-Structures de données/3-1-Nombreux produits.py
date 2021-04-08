nbDistributeurs = int(input())
nbOperations = int(input())

liste_D = [[0, []] for i in range(nbDistributeurs+1)]


for i in range(nbOperations):
    iDistributeur, operation, date = [int(x) for x in input().split(" ")]
    liste_D[iDistributeur][0] += operation
    if operation > 0:
        liste_D[iDistributeur][1].append([operation, date])

def recherche(liste, n):
    n -= liste[-1][0]
    if n > 0:
        return min(recherche(liste[:-1], n), liste[-1][1])
    else:
        return liste[-1][1]


liste = [""]*nbDistributeurs
for i in range(1, nbDistributeurs+1):
    som = liste_D[i][0]
    if som == 0:
        val = "0"
    else:
        val = str(recherche(liste_D[i][1], som))
    liste[i-1] = val

print("\n".join(liste))