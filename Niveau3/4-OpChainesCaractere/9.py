#Niveau 3.4 exercice 9
"""Par 4T"""
for ascii in range(ord("A"), ord("Z")+1):
   char = chr(ascii).lower()
   if char not in ["a","e","i","o","u","y"]:
      print(char, end=" ")








"""Correction de France-ioi"""
for ascii in range(ord('a'), ord('z') + 1):
   car = chr(ascii)
   if (car != "a" and car != "e" and car != "i" and
       car != "o" and car != "u" and car != "y"):
      if car != "z":
         print(car, end = " ")
      else:
         print(car)