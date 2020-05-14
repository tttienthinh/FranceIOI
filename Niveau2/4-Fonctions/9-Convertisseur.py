from sys import stdin




nb_valeur = int(input())
for i in range(nb_valeur):
   valeur, mesure = stdin.readline().split()
   valeur = float(valeur)
   if mesure == "m":
      print("{} p".format(str(valeur/0.3048)))
   elif mesure == "g":
      print("{} l".format(str(valeur*0.002205)))
   elif mesure == "c":
      print("{} f".format(str(valeur*1.8+32)))