def afficherEntier(nombre,base):
   chiffres = []
   while (nombre > 0) or (chiffres == []):
      chiffres = chiffres + [nombre % base]
      nombre = nombre // base
   for chiffre in reversed(chiffres):
      print(chiffre,end=" ")
   print()

def lireEntier(base):
   nombre = 0
   for chiffre in input().split():
      nombre = nombre * base + int(chiffre)
   return nombre
baseSource, baseCible, _ = map( int, input().split() )
afficherEntier( lireEntier(baseSource), baseCible )