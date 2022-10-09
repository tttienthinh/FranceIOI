import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

sql_query = input().replace(",", "").split()
m = len(sql_query)
rows = int(input())
table_header = input().split()
table = []
for i in range(rows):
    table.append(input().split())

# SELECT ... FROM ...
i = 1
n = len(table_header)
dico = {table_header[i]:i for i in range(n)}
columns = []
while sql_query[i] != "FROM":
    if sql_query[i] == "*":
        columns = [i for i in range(n)]
    else:
        columns.append(dico[sql_query[i]])
    i += 1
i += 2

# WHERE ... AND ... OR ...
indices = [True for i in range(rows)]
while i<m and sql_query[i] in ["WHERE", "AND", "OR"]:
    c = dico[sql_query[i+1]]
    val = sql_query[i+3]
    print(f"WHERE {c} {val}", file=sys.stderr, flush=True)
    if sql_query[i] in ["WHERE", "AND"]:
        for j in range(rows):
            if table[j][c] != val:
                indices[j] = False
    else:
        for j in range(rows):
            if table[j][c] == val:
                indices[j] = True
    i += 4

# ORDER BY ... DESC
indices = [i for i in range(rows) if indices[i]]
if i<m and sql_query[i] == "ORDER":
    i += 2
    c = dico[sql_query[i]]
    i += 1
    if i<m and sql_query[i]=="DESC":
        reverse=True
    else:
        reverse=False
    numerical = False
    for j in range(rows):
        if table[j][c].isnumeric():
            numerical = True

    def fonction(key):
        if numerical:
            return float(table[key][c])
        else:
            return table[key][c]

    print(f"reverse {reverse}", file=sys.stderr, flush=True)
    indices.sort(key=fonction, reverse=reverse)

# CREATION DE LA TABLE ET AFFICHAGE
answer = [[table_header[c] for c in columns]]
for i in indices:
    answer.append([table[i][c] for c in columns])

print("\n".join([" ".join(l) for l in answer]))