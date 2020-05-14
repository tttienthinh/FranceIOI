#Niveau 3.3 exercice 1
"""Par 4T"""
def converter(Base, origine, destination):
    for item in range(26):
        if origine[item] == Base:
            return (destination[item])


def main():
    nom = input()[0]
    age = input()
    alphabet = list(str('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    number = [str(item) for item in range(1, 27)]
    print(converter(nom, alphabet, number) + converter(age, number, alphabet))


main()








"""Correction de France-ioi"""
nomAuteur = input()
ageFils = int(input())
batiment = ord(nomAuteur[0]) - ord("A") + 1
allee = chr(ageFils - 1 + ord("A"))
print("{}{}".format(batiment, allee))