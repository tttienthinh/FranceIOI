def afficherBinaire(nombre):
   if nombre > 1:
      afficherBinaire(nombre // 2)
   print(nombre % 2,end="")
nbColonnes = int(input())
for ligne in range(1, nbColonnes + 1):
   for colonne in range(1, nbColonnes + 1):
      afficherBinaire(ligne*colonne)
      print("\t",end="")
   print()