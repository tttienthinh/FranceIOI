# %%
from sys import stdin
# %%
couple = []
for _, description in zip(range(3), stdin):
    X, Y = map(int, description.split())
    couple.append((X, Y))
# %%
# on travaille sur la hauteur issu de c du triangle abc
Xab, Yab = couple[1][0] - couple[0][0], couple[1][1] - couple[0][1]
Xac, Yac = couple[2][0] - couple[0][0], couple[2][1] - couple[0][1]

# vecteur normal
Xnab, Ynab = -Yab, Xab

# hauteur du triangle
if Xnab == 0 and Ynab == 0:
    print(0)
else:
    h = (Xac*Xnab + Yac*Ynab)/(Xnab**2 + Ynab**2)**0.5
    aire_2 = round(abs(h*(Xab**2 + Yab**2)**0.5))

    print(aire_2)
