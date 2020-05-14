from sys import stdin
def recursive(valeur, tim):
    if tim <= 0:
       print(valeur)
    else:
       recursive("["+valeur+"]", tim-1)

def main():
    valeur, tim = stdin.readline().split()
    tim = int(tim)
    recursive(valeur, tim)
main()