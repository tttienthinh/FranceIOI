nb_lignes = int(input())
for i in range(nb_lignes):
   phrase = input()
   for i in range(len(phrase)):
      print(phrase[-1-i], end="")
   print() 