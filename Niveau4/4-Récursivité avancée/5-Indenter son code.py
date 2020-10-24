# -*- coding: utf-8 -*-

L = input()

def recur(i, indent=""):
    while i < len(L):
        if L[i] == "{":
            print(indent+"{")
            i = recur(i+1, indent+"   ")
        elif L[i] == "}":
            print(indent[:-3]+"}")
            return i+1
recur(i=0)