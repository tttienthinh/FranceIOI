nbDeplacement = int(input())
liste = []
for i in range(nbDeplacement):
   liste.append(input())
for i in liste[::-1]:
   if i == "1":
      i = "2"
   elif i == "2":
      i = "1"
   elif i == "4":
      i = "5"
   elif i == "5":
      i = "4"
   print(i)