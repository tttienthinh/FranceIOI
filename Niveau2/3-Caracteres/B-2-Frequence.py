from sys import stdin
nb_ligne, nb_mot = stdin.readline().split()
dictionnaire = {}
for i in range(int(nb_ligne)):
   liste_mot = stdin.readline().split()
   for mot in liste_mot:
      try:
         dictionnaire[len(mot)] += 1
      except:
         dictionnaire[len(mot)] = 1
for i in range(101):
   try:
      print("{} : {}".format(i, dictionnaire[i]))
   except:
      sers_a_rien = 1