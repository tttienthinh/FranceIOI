N = int(input())

t_ligne = input()
t_ligne = t_ligne.split()
ligne = {}
for i, num in enumerate(t_ligne):
    ligne[i+1] = [int(num), -1 ]

code = input()
length = len(code)

def find(id):
    parent = ligne[id][0]
    if ligne[id][1] == -1:
        if parent == 0:
            ligne[id][1] = 0
        else:
            find(parent)
            ligne[id][1] = ligne[parent][1]+1

for num in range(1, len(ligne.copy())+1):
    find(num)

ligne = [ [k,v[1]] for k, v in ligne.items() ]
ligne.sort(key=lambda x: x[1])

out = []
for num, value in ligne:
    str_num = str(num)
    if length == len(str_num):
        matching = True
        for i in range(length):
            if not (code[i] == '?' or code[i]==str_num[i]):
                matching = False
                break
        if matching:
            out.append(str_num)
print(' '.join(out))

