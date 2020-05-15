import sys
input()

ligne = input().split()
ligne = [[int(num), -1 , i+1] for i, num in enumerate(ligne)]
print(sys.getsizeof(ligne))
code = input()
length = len(code)

def find(id):
    if ligne[id][1] == -1:
        if ligne[id][0] == 0:
            ligne[id][1] = 0
        else:
            find(ligne[id][0]-1)
            ligne[id][1] = ligne[ligne[id][0]-1][1]+1

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
            print(str_num, end=' ')
""" 
8
3 3 7 3 6 7 0 0
?
"""