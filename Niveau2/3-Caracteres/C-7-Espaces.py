liste_mot = input()
for caractere in liste_mot:
   if caractere == " ":
      print("_", end="")
   else:
      print(caractere, end="")