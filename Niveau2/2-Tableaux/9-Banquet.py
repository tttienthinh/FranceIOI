nbr_place = int(input())
nbr_deplacement = int(input())
liste_place = [input() for i in range(nbr_place)]
for i in range(nbr_deplacement):
   changement1 = int(input())
   changement2 = int(input())
   liste_place[changement1], liste_place[changement2] = liste_place[changement2], liste_place[changement1]
print("\n".join(liste_place))