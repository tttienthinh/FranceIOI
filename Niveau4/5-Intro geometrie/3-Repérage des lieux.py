from math import sqrt
from sys import stdin
def distance(x,y, x_,y_):
    return sqrt((x-x_)**2 + (y-y_)**2)
def vecteur(x,y, x_,y_):
    return (x_-x, y_-y)

XA, YA, XB, YB = [int(x) for x in input().split(" ")]
AB = distance(XA, YA, XB, YB)
vAB = vecteur(XA, YA, XB, YB)
N = int(input())

for _,description in zip(range(N),stdin):
    XC, YC = map(int,description.split())
    vAC = vecteur(XA, YA, XC, YC)
    
    # formule de ce site :
    # https://forums.commentcamarche.net/forum/affich-33681648-comment-calculer-un-angle-entre-trois-coordonnees-cartesiennes
    print((vAB[0]*vAC[0] + vAB[1]*vAC[1]) / AB)