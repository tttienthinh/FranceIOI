nombre,baseCible = map( int, input().split() )
chiffres = []
encoreUnChiffre = True
while encoreUnChiffre:
   chiffres = chiffres + [nombre % baseCible]
   nombre = nombre // baseCible
   encoreUnChiffre = (nombre > 0)
print(len(chiffres))
for chiffre in reversed(chiffres):
   print(chiffre,end=" ")
print()