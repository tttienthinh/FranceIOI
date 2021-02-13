from sys import stdin

XA, YA, XB, YB = [int(x) for x in input().split(" ")]
Xab = XB-XA
Yab = YB-YA

N = int(input())



if Xab == 0:
    a = 1
    b = 0
    c = - XA
else:
    a = Yab/Xab
    b = -1
    c = -(a*XA + b*YA)

distance = lambda a, b, c, XC, YC: abs(a*XC + b*YC + c) / (a**2 + b**2)**0.5


d_max = 0
couple = None
for _, description in zip(range(N), stdin):
    XC, YC = map(int, description.split())
    d = distance(a, b, c, XC, YC)
    if d > d_max:
        couple = [XC, YC]
        d_max = d
print(" ".join([str(x) for x in couple]))
