# %%
from sys import stdin
# %%
X, Y = [int(x) for x in input().split(" ")]
# %%
N = int(input())
# %%
def distance_droite(Xa, Ya, Xb, Yb):
    Xab = Xb-Xa
    Yab = Yb-Ya

    if Xab == 0:
        a = 1
        b = 0
        c = - Xa
    else:
        a = Yab/Xab
        b = -1
        c = -(a*Xa + b*Ya)

    return abs(a*X + b*Y + c) / (a**2 + b**2)**0.5
# %%
def distance(Xa, Ya, Xb, Yb):
    Xap, Yap = X-Xa, Y-Ya
    Xbp, Ybp = X-Xb, Y-Yb
    da = ((Xap)**2 + (Yap)**2)**0.5
    db = ((Xbp)**2 + (Ybp)**2)**0.5
    Xab, Yab = Xb-Xa, Yb-Ya
    dd = distance_droite(Xa, Ya, Xb, Yb)
    if -(Xab*Xap + Yab*Yap) < 0 and -(- Xab*Xbp - Yab*Ybp) < 0: # Test 
        response = min(da, db, dd)
    else:
        response = min(da, db)
    return response
# %%
d_min = float("inf")
couple = []
for _, description in zip(range(N), stdin):
    Xa, Ya, Xb, Yb = map(int, description.split())
    d = distance (Xa, Ya, Xb, Yb)
    if d < d_min:
        d_min = d
        couple = [Xa, Ya, Xb, Yb]
print(" ".join([str(x) for x in couple]))