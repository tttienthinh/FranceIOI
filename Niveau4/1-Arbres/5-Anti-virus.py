import sys
N = int(input())

ligne = input()
ligne = ligne.split()
ligne = [[int(num), -1 , i+1] for i, num in enumerate(ligne)]

code = input()
length = len(code)

def find(id):
    parent = ligne[id][0]-1
    if ligne[id][1] == -1:
        if parent == -1:
            ligne[id][1] = 0
        else:
            find(parent)
            ligne[id][1] = ligne[parent][1]+1

for num in range(len(ligne.copy())):
    find(num)

ligne.sort(key=lambda x: x[1])


for recipient, value, num in ligne:
    str_num = str(num)
    if length == len(str_num):
        matching = True
        for i in range(length):
            if not (code[i] == '?' or code[i]==str_num[i]):
                matching = False
                break
        if matching:
            stdout.write('{} '.format(str_num))
""" 
8
3 3 7 3 6 7 0 0
?
"""