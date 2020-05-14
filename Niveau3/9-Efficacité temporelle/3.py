

from sys import stdin

input = stdin.readline


def main():
    X_MAX = 100
    Y_MAX = 100
    nbPoints = int(input())
    estUnPoint = [[False] * 101 for _ in range(101)]
    points = [None] * nbPoints
    for iPoint in range(nbPoints):
        x, y = map(int, input().split())
        points[iPoint] = x, y
        estUnPoint[x][y] = True
    points.sort()
    nbMilieux = 0
    for iMilieu in range(nbPoints):
        xMilieu, yMilieu = points[iMilieu]
        deuxXMilieu = xMilieu * 2
        deuxYMilieu = yMilieu * 2
        for iExtrémité in range(iMilieu):
            xExtrémité, yExtrémité = points[iExtrémité]
            xAutre = deuxXMilieu - xExtrémité
            yAutre = deuxYMilieu - yExtrémité
            if 0 <= xAutre <= X_MAX and 0 <= yAutre <= Y_MAX and \
                    estUnPoint[xAutre][yAutre]:
                nbMilieux += 1
                break
    print(nbMilieux)


main()