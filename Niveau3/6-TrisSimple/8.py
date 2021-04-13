from sys import stdin, stdout
input = stdin.readline

n = int(input())
liste = [int(x) for x in input().split()]
liste.sort()


q = int(input())
for k in range(q):
   question = int(input())
   if question < liste[0] or liste[-1] < question:
      stdout.write("0\n")
   else:
      i, j = 0, n-1
      result = "0\n"
      while i <= j:
         l = (i + j)//2
         if question == liste[l]:
            result = "1\n"
            j = i-1
         elif question < liste[l]:
            j = l-1
         else:
            i = l+1
      stdout.write(result)