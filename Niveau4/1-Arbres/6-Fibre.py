import numpy as np

N = 10
A = np.array([[0]*N]*N)
for i in range(N):
    A[i, i] = 1

for i in range(N-1):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    A[a, b] = 1
    A[b, a] = 1
B = A.copy()
B[2, 6] = 0
B[6, 2] = 0
a = 0
trouve = False
while not trouve:
    for i in range(N):
        if sum(A[i] == 0) <= 0:
            print(i)
            trouve = True
            break
    a += 1
    A = np.dot(A, A)
print(a)
print(A)

for i in range(3):
    B = np.dot(B, B)

print(B)