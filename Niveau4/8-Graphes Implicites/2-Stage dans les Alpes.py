K, N = map(int, input().split())

def rec(k, n, m):
    if n == 0:
        print(m)
    else:
        for i in range(k, K+1):
            rec(i, n-1, m+"{} ".format(i))
rec(1, N, "")