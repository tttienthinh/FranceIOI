from sys import stdin
def recursive(nbrFois, reponse):
    if nbrFois <= 0:
        print("0 = "+reponse)
    else:
        recursive(nbrFois-1, "("+reponse+" + "+reponse+")")

nbrFois = int(stdin.readline()[:-1])
recursive(nbrFois, "0")