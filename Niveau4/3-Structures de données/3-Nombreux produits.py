nbDistributeurs = int(input())
nbOperations = int(input())

liste_D = [[] for i in range(nbDistributeurs+1)]

def retirer(liste, val):
    i = 0
    while val > 0:
        if liste[i][1] > val:
            liste[i][1] = liste[i][1] - val
            val = 0
        else:
            val -= liste[i][1]
            liste[i][1] = 0
            i += 1
    return liste[i:]

for i in range(nbOperations):
    iDistributeur, operation, date = [int(x) for x in input().split(" ")]
    if operation > 0:
        liste_D[iDistributeur].append([date, operation])
    else:
        liste_D[iDistributeur] = retirer(liste_D[iDistributeur], -operation)

liste = [""]*nbDistributeurs
for i in range(1, nbDistributeurs+1):
    if liste_D[i] == []:
        val = "0"
    else:
        val = str(min(liste_D[i])[0])
    liste[i-1] = val

print("\n".join(liste))