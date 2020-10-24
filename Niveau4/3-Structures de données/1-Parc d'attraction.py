N, R = [int(x) for x in input().split(" ")]
liste = []
for x in input().split(" "):
    try:
        liste.append(int(x))
    except:
        pass

for i in range(R):
    a, b = [int(x) for x in input().split(" ")]
    print(sum(liste[a-1:b]))