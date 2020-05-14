cartes1 = input()
cartes2 = input()
if cartes1 == cartes2:
   print("=")
   print(len(cartes1))
else: 
   egalite = 0
   winner = "="
   i=0
   while True:
      try:
         caractere1 = cartes1[i]
      except:
         winner = 2
         break
      try:
         caractere2 = cartes2[i]
      except:
         winner = 1
         break
      if caractere1 == caractere2:
         egalite += 1
         i += 1
      elif caractere1 < caractere2:
         winner = 1
         break
      else:
         winner = 2
         break
   print(winner)
   print(egalite)