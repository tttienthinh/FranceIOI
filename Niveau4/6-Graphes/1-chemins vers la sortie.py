from copy import deepcopy

L, C = [int(x) for x in input().split(" ")]

tableau = []
for _ in range(L):
    tableau.append(list(input()))

# L, C = 10, 10
# tableau = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '.', '.', '#', '.', '#', '.', '#'], ['#', '.', '#', '#', '#', '.', '.', '.', '#', '#'], ['#', '.', '#', '.', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '#', '#', '#', '#', '.', '#'], ['#', '.', '#', '.', '.', '.', '.', '.', '#', '#'], ['#', '.', '.', '#', '.', '.', '#', '.', '.', '#'], ['#', '.', '.', '.', '#', '.', '.', '#', '.', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#']]

def recur(tableau, pos=(1, 0)):
    if pos == (L-1, C-2):
        return 1
    n_tableau = deepcopy(tableau)
    n_tableau[pos[0]][pos[1]] = "#"
    possibility = 0
    if pos[0]>1 and tableau[pos[0]-1][pos[1]] == ".":
        possibility += recur(n_tableau, (pos[0]-1, pos[1]))
    if pos[0]<C-1 and tableau[pos[0]+1][pos[1]] == ".":
        possibility += recur(n_tableau, (pos[0]+1, pos[1]))
        
    if pos[1]>1 and tableau[pos[0]][pos[1]-1] == ".":
        possibility += recur(n_tableau, (pos[0], pos[1]-1))
    if pos[1]<L-1 and tableau[pos[0]][pos[1]+1] == ".":
        possibility += recur(n_tableau, (pos[0], pos[1]+1))
        
    return possibility

print(recur(tableau))