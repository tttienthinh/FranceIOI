TaxeActuelle = float(input())/100
TaxeFuture = float(input())/100
PrixActuel = float(input())
PrixLégume = (PrixActuel / (TaxeActuelle+1))
PrixFutur = round(PrixLégume* (TaxeFuture+1), 2)
print(PrixFutur)