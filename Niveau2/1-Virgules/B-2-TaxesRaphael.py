taxe1=float(input())
taxe2=float(input())
prixtx=float(input())

prixht=prixtx / (1+taxe1/100)

prixttc=prixht * (1+taxe2/100)

prixttc=prixttc*100

prixttc=round(prixttc)

prixttc=prixttc/100

print(prixttc)