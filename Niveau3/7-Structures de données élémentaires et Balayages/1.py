from sys import stdin
def main():
    stdin.readline()
    ListeProduit = [int(element) for element in stdin.readline().split()]
    for i in range(int(input())):
        Produit, Transaction = [int(valeur) for valeur in stdin.readline().split()]
        ListeProduit[Produit-1] += Transaction
    print(" ".join([str(quantite) for quantite in ListeProduit]))
main()