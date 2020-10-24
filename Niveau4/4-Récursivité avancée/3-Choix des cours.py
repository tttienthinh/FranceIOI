# N, L = [int(x) for x in input().split(" ")]
N = 5
L = 3
def recur(Liste, i, cours):
    if i==0:
        print(" ".join(cours))
    else:
        for x in range(len(Liste)):
            if len(Liste[x:]) >= i:
                recur(Liste[x+1:], i-1, cours+[str(Liste[x])])
                
recur(list(range(1, N+1)), L, [])