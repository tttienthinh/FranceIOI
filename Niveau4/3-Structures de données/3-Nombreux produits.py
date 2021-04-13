from sys import stdout, stdin
input = stdin.readline
nbDistributeurs = int(input())
nbOperations = int(input())

liste_D = [[0, [], 99999999] for i in range(nbDistributeurs+1)]

for i in range(nbOperations):
    iDistributeur, operation, date = [int(x) for x in input().split(" ")]
    op = liste_D[iDistributeur][0] + operation
    liste_D[iDistributeur][0] = op
    if operation > 0:
        n = len(liste_D[iDistributeur][1])
        if liste_D[iDistributeur][2] >= date:
            liste_D[iDistributeur][1] = []
            liste_D[iDistributeur][2] = date
        elif op < n:
            liste_D[iDistributeur][1] = liste_D[iDistributeur][1][n-op:]
        liste_D[iDistributeur][1].append([operation, date])

for i in range(1, nbDistributeurs+1):
    som = liste_D[i][0]
    if som == 0:
        val = 0
    else:
        l_ = liste_D[i][1][-1]
        val = l_[1]
        n = som - l_[0]
        j = 1
        length = len(liste_D[i][1])
        while n > 0 and j < length:
            j += 1
            l_ = liste_D[i][1][-j]
            val = min(val, l_[1])
            n -= l_[0]
    stdout.write("%d\n" %val)