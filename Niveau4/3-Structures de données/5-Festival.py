from sys import stdin, stdout
input = stdin.readline

nbJours, nbGroupes = map(int, input().split())

groupes = [0 for i in range(nbGroupes)]
jours = [int(x) for x in input().split()]

i, j = 0, 0
mini = nbJours
while True:
    if j-i < nbGroupes or 0 in groupes:
        if j < nbJours:
            groupes[jours[j] - 1] += 1
            j += 1
        else:
            break
    else:
        mini = min(mini, j - i)
        groupes[jours[i] - 1] -= 1
        i += 1
stdout.write("%d" % mini)
