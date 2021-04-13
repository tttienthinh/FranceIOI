
L, C = [int(x) for x in input().split(" ")]
tableau = [list(input()) for i in range(L)]


def sortie(x, y):
    if (x, y) == (C-2, L-2):
        return 1
    else:
        tableau[y][x] = "?"
        count = 0
        for (i, j) in [(-1,0),(1,0),(0,-1),(0,1)]:
            x_ = x + i
            y_ = y + j
            if tableau[y_][x_] == ".":
                count += sortie(x_, y_)
        tableau[y][x] = "."
        return count

print(sortie(1, 1))




"""
autre idée réutilisant quand cela est possible les chemins déjà calculé

L, C = [int(x) for x in input().split(" ")]
tableau = [list(input()) for i in range(L)]

L, C = 10, 10
tableau = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
    ['#', '#', '#', '.', '.', '#', '.', '#', '.', '#'], 
    ['#', '.', '#', '#', '#', '.', '.', '.', '#', '#'], 
    ['#', '.', '#', '.', '.', '.', '#', '.', '.', '#'], 
    ['#', '.', '.', '.', '#', '#', '#', '.', '.', '#'], 
    ['#', '.', '#', '.', '.', '.', '.', '.', '#', '#'], 
    ['#', '.', '.', '#', '.', '.', '#', '.', '.', '#'], 
    ['#', '.', '.', '.', '#', '.', '.', '#', '.', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#']
]

for x in tableau:
    print("".join(str(y) for y in x))

def sortie(_y, _x, y, x):
    if (x, y) == (C-2, L-2):
        return 1, True
    elif tableau[y][x] == "#":
        return 0, True
    elif tableau[y][x] == ".":
        tableau[y][x] = "?"
        count = 0
        checked = True
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            y_ = y + i
            x_ = x + j
            if (_x, _y) != (x_, y_) and x_ > 0 and x_ < C-1 and y_ > 0 and y_ < L:
                count_, checked_ = sortie(y, x, y_, x_)
                count += count_
                checked = checked and checked_
        
        if checked:
            tableau[y][x] = count
        else:
            tableau[y][x] = "."
        
        for x in tableau:   
            print("".join(str(y) for y in x))
        input()
        
        return count, checked
    elif tableau[y][x] == "?":
        return 0, False
    else:
        return tableau[y][x], True

print(sortie(1, 0, 1, 1)[0])
"""
