def ligne(nb_X):
   for i in range(nb_X):
      print("X", end="")

def rectangle(lig, col):
   liste = [[" "]*col]*lig
   liste[0] = ["#" for i in range(col)]
   liste[-1] = ["#" for i in range(col)]
   for i in range(1,lig-1):
      liste[i][0] = "#"
      liste[i][-1] = "#"
   for i in range(lig):
      print("".join(liste[i]))

def triangle(cote):
   liste = [[" "]*(i+1) for i in range(cote)]
   liste[cote-1] = ["@"]*cote
   for i in range(cote):
      liste[i][0] = "@"
      liste[i][-1] = "@"
   for i in range(cote):
      print("".join(liste[i]))

ligne(int(input()))
print("\n"*2)
rectangle(int(input()), int(input()))
print()
triangle(int(input()))