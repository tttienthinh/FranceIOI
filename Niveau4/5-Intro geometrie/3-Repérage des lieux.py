from sys import stdin, stdout
from math import sqrt

XA, YA, XB, YB = [int(x) for x in input().split(" ")]
Xab = XB-XA
Yab = YB-YA
AB = sqrt(Xab**2 + Yab**2)
N = int(input())

for _, description in zip(range(N), stdin):
    XC, YC = map(int, description.split())
    stdout.write(str(round((Xab*(XC-XA) + Yab*(YC-YA)) / AB, 4)))
