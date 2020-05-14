from sys import stdin

def main():
    nbrValeur = int(input())
    liste_input = list(set([int(i) for i in stdin.readline().split()]))
    liste_input.sort()
    nbrValeur = len(liste_input)
    nbr_fois = int(input())

    for i in range(nbr_fois):
        demande = int(input())
        borne_inf_index = 0
        borne_sup_index = nbrValeur-1

        borne_inf = liste_input[borne_inf_index]
        borne_sup = liste_input[borne_sup_index]

        ecart_borne_inf = demande - borne_inf
        ecart_borne_sup = borne_sup - demande

        if ecart_borne_inf == 0:
            print(borne_inf)
        elif ecart_borne_sup == 0:
            print(borne_sup)
        else:

            while True:
                new_borne_index = int((borne_inf_index + borne_sup_index) / 2)
                new_borne = liste_input[new_borne_index]

                ecart_new_borne = demande - new_borne

                if ecart_new_borne < 0:
                    borne_sup_index = new_borne_index
                    borne_sup = new_borne
                    ecart_borne_sup = -1 * ecart_new_borne
                elif ecart_new_borne > 0:
                    borne_inf_index = new_borne_index
                    borne_inf = new_borne
                    ecart_borne_inf = ecart_new_borne
                else:
                    print(new_borne)
                    break

                if borne_sup_index - borne_inf_index == 1:
                    if ecart_borne_inf <= ecart_borne_sup:
                        print(borne_inf)
                    else:
                        print(borne_sup)
                    break


main()