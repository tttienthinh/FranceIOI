

n = int(input())
ligne = input().split()
ligne = [int(i) for i in ligne]
code = input()


table = [-1] * (n+1)


def find(i):
    try:
        if table[i] >= 0:
            return table[i]+1
        elif i == 0:
            return 0
        else:
            p = 1 + find(ligne[i - 1])
            table[i] = p
            return p
    except:
        print(i)



def create(text, i, l):
    while i < l and text[i] != "?":
        i += 1
    if i == l:
        return [text]
    a = 0
    list_text = []
    if i == 0:
        a = 1
    for c in range(a, 10):
        text[i] = c
        list_text += create(text.copy(), i + 1, l)
    return list_text


text = list(code)
l = len(text)
t = [int(''.join(map(str, t))) for t in create(text.copy(), 0, l)]
classement = {}
path = []
for i in t:
    if i < n:
        a = find(i)
        if a in path:
            classement[a].append(i)
        else:
            classement[a] = [i]
            path.append(a)
path.sort()
text = []
for a in path:
    text += classement[a]
print(' '.join(map(str, text)))



