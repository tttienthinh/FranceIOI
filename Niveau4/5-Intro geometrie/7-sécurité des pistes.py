# %%
def eq(XA, YA, XB, YB): # donne les coefficients générales d'une droite
    
    Xab = XB-XA
    Yab = YB-YA

    if Xab == 0:
        a = 0
        b = 1
        c = XA
    else:
        a = Yab/Xab
        b = -1
        c = a*XA + b*YA
    return (a, b, c)
# %%
# Première droite eq° : a1 X + b1 Y = c1
XA1, YA1, XB1, YB1 = [int(x) for x in input().split(" ")]
a1, b1, c1 = eq(XA1, YA1, XB1, YB1)
# Deuxième droite eq° : a2 X + b2 Y = c2
XA2, YA2, XB2, YB2 = [int(x) for x in input().split(" ")]
a2, b2, c2 = eq(XA2, YA2, XB2, YB2)
# %%
# méthode de résolution système à 2 équation de Cramer
det = lambda x, y, x_, y_: x*y_ - x_*y
# %%
# calcul du déterminant != 0
d = det(a1, b1, a2, b2)
if d == 0:
    if a1 != 0:
        X, Y = (c1-b1*YA1)/a1, YA1
    elif a2 != 0:
        X, Y = (c2-b1*YA1)/a2, YA1
    elif b1 != 0:
        X, Y = XA1, (c1-a1*XA1)/b1
    elif b2 != 0:
        X, Y = XA1, (c2-a2*XA1)/b2
else:
    X = det(c1, b1, c2, b2) / d
    Y = det(a1, c1, a2, b2) / d

# %%
print(round(X, 4), round(Y, 4))

""" Corrections très efficace """
"""
xA,yA, xB,yB = map(int,input().split())
xC,yC, xD,yD = map(int,input().split())
xAB = xB - xA
yAB = yB - yA
xCD = xD - xC
yCD = yD - yC
xAC = xC - xA
yAC = yC - yA
t = ( xAC * yCD - yAC * xCD ) / ( xAB * yCD - yAB * xCD )
print( xA + t * xAB, yA + t * yAB )
"""
