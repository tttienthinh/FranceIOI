import sys


def main():
    nb_requetes = int(input())
    nbAffiches = 0
    affiches = [0] * nb_requetes
    for requete, _ in zip(sys.stdin, range(nb_requetes)):
        requete = requete.split()
        if requete[0] == 'Q':
            print(nbAffiches)
        else:
            affiche = int(requete[1])
            while (nbAffiches > 0) and (affiches[nbAffiches - 1] <= affiche):
                nbAffiches -= 1
            affiches[nbAffiches] = affiche
            nbAffiches += 1


main()