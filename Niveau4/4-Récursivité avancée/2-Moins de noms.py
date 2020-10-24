l = int(input())
lettre = input()
n = int(input())

def recur(L, i, nom=""):
    liste = []
    if i == 0:
        return [nom]
    else:
        for x in L:
            if not x in nom:
                liste += recur(L, i-1, nom+x)
        return liste

liste = recur(lettre, n)
print(len(liste))
print("\n".join(liste))