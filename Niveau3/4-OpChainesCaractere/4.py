#Niveau 3.4 exercice 4
"""Par 4T"""
def main():
   dic = {}
   liste = []
   for i in range(int(input())):
      entre = input().split(" ")
      dic[entre[1]] = entre[0]
   for item in dic.items():
      liste.append(item[0])
   liste.sort()
   for key in liste:
      print("{} {}".format(key, dic[key]))

main()








"""Correction de France-ioi"""
nbMots = int(input())
couplesMots = [""] * nbMots
for idCouple in range(nbMots):
   premier, second = input().split(" ")
   couplesMots[idCouple] = second + " " + premier
couplesMots.sort()
for idCouple in range(nbMots):
   print(couplesMots[idCouple])