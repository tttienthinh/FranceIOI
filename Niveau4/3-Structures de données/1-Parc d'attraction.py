N, R = [int(x) for x in input().split(" ")]
histo = [0]
for x in input().split(" "):
    if x != "\r":
        histo.append(histo[-1] + int(x))

liste = []
for i in range(R):
    a, b = [int(x) for x in input().split(" ")]
    liste.append(str(histo[b]-histo[a-1]))

print("\n".join(liste))

"""
Correction proposée 

import sys
def main():
   nbJours,nbPeriodes = map(int,input().split())
   
   nbVisiteursCumules = [0]*(nbJours + 1)
   cumul = 0
   for jour,nombre in enumerate(input().split(),1):
      cumul += int(nombre)
      nbVisiteursCumules[jour] = cumul
   
   def reponses():
      for periode,_ in zip(sys.stdin,range(nbPeriodes)):
         debut,fin = map(int,periode.split())
         yield (nbVisiteursCumules[fin]-nbVisiteursCumules[debut-1])
   
   print("\n".join( map(str,reponses()) ))
   
main()

"""