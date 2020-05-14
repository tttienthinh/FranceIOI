nb_livre = int(input())
longueur = 0
for i in range(nb_livre):
   livre = input()
   if len(livre) > longueur:
      print(livre)
      longueur = len(livre)