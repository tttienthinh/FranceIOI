# -*- coding: utf-8 -*-

text = input()
liste_open  = {'(': ')', '[': ']', '{': '}', '<': '>'}
liste_close = [')', ']', '}', '>']

def test(end="", i=0):
    validate = True
    while i < len(text):
        x = text[i] 
        if x in liste_open:
            validate, i = test(liste_open[x], i+1)
            if not validate:
                return False, i+1
        elif x in liste_close:
            if x == end:
                return True, i+1
            else:
                return False, i+1
        else:
            i += 1
    if end=="":
        return True, i
    else:
        return False, i
    
validate, i = test()
if validate:
    print("yes")
else:
    print("no")
#include  int main(){int liste[2] = {1, 4}; return (liste[0] + liste[1]);}