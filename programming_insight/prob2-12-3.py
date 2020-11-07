
def kString(n, k):
    if n < 1:
        print("%s" % A)
    else:
        for j in range(k):
            A[n-1] = j
            kString(n-1, k)

A = []
a, b = map(int, input().split())
for i in range(a):
    A.append("")

kString(a, b)
