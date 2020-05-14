nombreBinaire = input()
nombreDécimal = 0
for chiffre in nombreBinaire:
   nombreDécimal = (nombreDécimal * 2) + int(chiffre)
print(nombreDécimal)