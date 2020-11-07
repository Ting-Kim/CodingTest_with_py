def binary(n):

    if n < 1:
        print("%s" % A)
    else :
        A[n-1] = 0
        binary(n-1)
        A[n-1] = 1
        binary(n-1)



A = []

a = int(input())
for i in range(a):
    A.append("")

binary(a)

