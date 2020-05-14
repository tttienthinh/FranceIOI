from sys import stdin
def main():
    nbr_operation = int(stdin.readline()[:-1])
    liste_peremption = []
    for i in range(nbr_operation):
        action, peremption = [int(element) for element in stdin.readline().split()]
        action = int(action)
        peremption = int(peremption)
        if action < 0:
            liste_peremption = liste_peremption[-action:]
        else:
            liste_peremption += [peremption for _ in range(action)]
    liste_peremption.sort()
    print(liste_peremption[0])
main()




"""correction"""
from sys import stdin
def main():
    MAX_PRODUITS = 1000
    produits = [0] * MAX_PRODUITS
    posExtract, posInsert = 0, 0
    nbOperations = int(input())
    for _ in range(nbOperations):
        quantite, date = map(int, stdin.readline().split())
        if quantite > 0:
            for _ in range(quantite):
                produits[posInsert] = date
                posInsert = (posInsert + 1) % MAX_PRODUITS
        else:
            posExtract = (posExtract - quantite) % MAX_PRODUITS
    dateMin = produits[posExtract]
    posExtract = (posExtract + 1) % MAX_PRODUITS
    while posExtract != posInsert:
        dateMin = min(dateMin, produits[posExtract])
        posExtract = (posExtract + 1) % MAX_PRODUITS
    print(dateMin)
main()