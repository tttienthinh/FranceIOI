from math import sqrt
X, Y = [int(x) for x in input().split(" ")]
N = int(input())

def distance(x,y, x_,y_):
    return sqrt((x-x_)**2 + (y-y_)**2)

X_, Y_ = [int(x) for x in input().split(" ")]
result = (X_, Y_)
mini = distance(X, Y, X_, Y_)

for i in range(N-1):
    X_, Y_ = [int(x) for x in input().split(" ")]
    dist = distance(X, Y, X_, Y_)
    if dist<mini:
        result = (X_, Y_)
        mini = dist

print(result[0], result[1])


