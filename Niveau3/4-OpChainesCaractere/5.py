#Niveau 3.4 exercice 5
"""Par 4T"""
liste = []
while True:
   try:
      liste += input().split(" ")
   except:
      print(sum(int(item) for item in liste))
      break








"""Correction de France-ioi"""
estFini = False
nbTotal = 0
while not estFini:
   try:
      journee = input()
   except:
      estFini = True
   if not estFini:
      for nbGens in map(int, journee.split(" ")):
         nbTotal = nbTotal + nbGens
print(nbTotal)