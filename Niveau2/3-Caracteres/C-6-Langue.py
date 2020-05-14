caractere = input()
nb_ligne = int(input())
counter = 0
for i in range(nb_ligne):
   ligne = input()
   for lettre in ligne:
      if lettre == caractere:
         counter += 1
print(counter)