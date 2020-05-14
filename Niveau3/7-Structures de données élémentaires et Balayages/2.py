from sys import stdin
def main():
    nbr_operation = int(stdin.readline()[:-1])
    liste_peremption = []
    for i in range(nbr_operation):
        action, peremption = [int(element) for element in stdin.readline().split()]
        action = int(action)
        peremption = int(peremption)
        if action < 0:
            liste_peremption = liste_peremption[:action]
        else:
            liste_peremption += [peremption for _ in range(action)]
    liste_peremption.sort()
    print(liste_peremption[0])
main()