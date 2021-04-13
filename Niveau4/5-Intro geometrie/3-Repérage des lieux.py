from sys import stdin, stdout
from math import sqrt

XA, YA, XB, YB = map(int, input().split())
Xab = XB-XA
Yab = YB-YA
AB = sqrt(Xab**2 + Yab**2)
N = int(input())
for _, description in zip(range(N), stdin):
    XC, YC = map(int, description.split())
    stdout.write("%f\n" %((Xab*(XC-XA) + Yab*(YC-YA)) / AB))
