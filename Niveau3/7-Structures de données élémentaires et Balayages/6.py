from sys import stdin
nb_hydro, nb_longueur = stdin.readline().split()
nb_hydro, nb_longueur = int(nb_hydro), int(nb_longueur)
liste = stdin.readline().split()
liste_valeur = [int(i) for i in liste]
somme = sum(liste_valeur[0:nb_hydro])
best = somme
for i in range(1, nb_longueur - nb_hydro):
   somme += liste_valeur[i+nb_hydro-1] - liste_valeur[i-1]
   if somme > best:
      best = somme
if best == 0:
   print("10")
else:
   print(best)