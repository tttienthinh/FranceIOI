# -*- coding: utf-8 -*-

dictionnaire = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y,
        "/": lambda x, y: x/y,
        "%": lambda x, y: x%y,
        }
L = input()

def number(i, a):
    x = L[i]
    if x.isnumeric():
        return number(i+1, a+x)
    else:
        return a, i
        
def recur(i=0):
    while i<len(L):
        x = L[i]
        if x in dictionnaire:
            
        elif x == "(":
            i = recur(i+1)
        elif x == ")":
            return i+1, result