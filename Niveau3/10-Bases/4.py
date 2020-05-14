baseSource, nbChiffres = map( int, input().split() )
nombreDécimal = 0
chiffres = map( int, input().split() )
for chiffre in chiffres:
   nombreDécimal = (nombreDécimal * baseSource) + chiffre
print(nombreDécimal)