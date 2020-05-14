def afficherBinaire(nombre):
   if nombre > 1:
      afficherBinaire(nombre // 2)
   print(nombre % 2,end="")

nombre = int(input())
afficherBinaire(nombre)