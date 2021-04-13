from sys import stdin, stdout
input = stdin.readline

nbEmissions, dureeMax = [int(x) for x in input().split()]
liste = [int(x) for x in input().split()]

maxi = 0
n = 0
val = 0
i = 0
j = 0

while j < nbEmissions:
   if val < dureeMax:
      val += liste[j]
      j += 1
   else:
      val -= liste[i]
      i += 1
   if val <= dureeMax and n < j-i:
      maxi = val
      n = j-i
print(n)
