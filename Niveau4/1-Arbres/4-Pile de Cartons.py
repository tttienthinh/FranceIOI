nbCartons = int(input())

def find(catalogue, id):
    ligne = catalogue[id]
    for number in ligne:
        print('A ', number)
        find(catalogue, number)
        print('R ', number)

catalogue = []
for i in range(nbCartons+1):
    ligne = input()
    ligne = ligne.split()
    try:
        ligne = [int(number) for number in ligne]
    except:
        print(ligne)
    catalogue.append(ligne[1:])
find(catalogue, 0)
