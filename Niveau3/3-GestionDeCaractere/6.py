#Niveau 3.3 exercice 6
"""Par 4T"""
def Verification(nom):
    if nom[0].isalpha() or nom[0] == "_":
        for caracter in nom[1:]:
            if not (caracter.isdigit() or caracter.isalpha() or caracter == "_"):
                return (False)
        return (True)
    else:
        return (False)

def main():
    for i in range(int(input())):
        nom = input()
        if Verification(nom):
            print("YES")
        else:
            print("NO")

main()








"""Correction de France-ioi"""
nbIdentifiants = int(input())
for loop in range(nbIdentifiants):
   estValide = True
   identifiant = input()
   if not (identifiant[0].isalpha() or (identifiant[0] == "_")):
      estValide = False
   for idCaractere in range(1, len(identifiant)):
      caractere = identifiant[idCaractere];
      if not (caractere.isalpha() or caractere.isdigit() or (caractere == '_')):
         estValide = False
   if estValide:
      print("YES")
   else:
      print("NO")