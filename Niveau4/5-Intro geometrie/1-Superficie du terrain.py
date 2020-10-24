X1, Y1, X2, Y2 = [int(x) for x in input().split(" ")]
surface = (X2-X1) * (Y2-Y1)
N = int(input())

for i in range(N):
    X1_, Y1_, X2_, Y2_ = [int(x) for x in input().split(" ")]
    if not(X2_<X1 or X1_>X2 or Y2_<Y1 or Y1_>Y2):
        if X1_<X1:
            X1_ = X1
        if X2_>X2:
            X2_ = X2
        if Y1_<Y1:
            Y1_ = Y1
        if Y2_>Y2:
            Y2_ = Y2
        surface -= (X2_-X1_) * (Y2_-Y1_)
print(surface)

