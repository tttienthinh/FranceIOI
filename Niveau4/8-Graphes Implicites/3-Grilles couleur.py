from sys import stdin, setrecursionlimit
  
setrecursionlimit(10**7)
input = stdin.readline

L, H = map(int, input().split())
tableau = [list(input()) for i in range(L)]
dejaVisit = [(0, 0, L-1, H-1)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]

def valid(x, y):
    return (x >= 0 and y >= 0 and x <= L-1 and y <= H-1)

def possible(x, y, z, t):
    global dejaVisit
    if (x, y) == (L-1, H-1) and (z, t) == (0, 0):
        return True
    else:
        dejaVisit.append((x, y, z, t))
        checker = False
        for dx, dy in delta:
            for dz, dt in delta:
                x_, y_ = x+dx, y+dy
                z_, t_ = z+dz, t+dt
                if not checker and valid(x_, y_) and valid(z_, t_):
                    if not checker and tableau[y_][x_] == tableau[t_][z_] and not (x_, y_, z_, t_) in dejaVisit:
                        checker = possible(x_, y_, z_, t_)
        dejaVisit = dejaVisit[:-1]
        return checker

if possible(0, 0, L-1, H-1):
    print("1")
else:
    print("0")
