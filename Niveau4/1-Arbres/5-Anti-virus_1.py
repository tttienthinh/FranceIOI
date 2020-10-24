n = int(input())

dictionnaire = {i:[] for i in range(n+1)}
for i, x in enumerate(input().split()):
    dictionnaire[int(x)].append(i+1)
    
code = input()
length = len(code)
liste_fixe = []
for i in range(length):
    if code[i] != "?":
        liste_fixe.append(i)

sortie = []
inter = dictionnaire[0]

while len(inter)>0:
    n_inter = []
    for i in inter:
        n_inter += dictionnaire[i]
        x = str(i)
        if len(x) == length:
            valide = True
            for i in range(length):
                if code[i]!="?" and x[i] != code[i]:
                    valide = False
                    break
            if valide:
                sortie.append(x)
    inter = n_inter.copy()

print(" ".join(sortie))