# -*- coding: utf-8 -*-

l = int(input())
lettre = input()
n = int(input())

def recur(L, i, nom=""):
    if i == 0:
        print(nom)
    else:
        for x in L:
            recur(L, i-1, nom+x)
print(l**n)
recur(lettre, n)