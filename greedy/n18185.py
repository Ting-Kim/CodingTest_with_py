# greedy problem no.1
# acmicpc.net 18185번 라면 사기(Small)

def three(arr, index):
    global cost
    if arr[index] != 0 and arr[index+1] != 0 and arr[index+2] != 0:
            a = min(arr[index], arr[index+1], arr[index+2])
            for i in range(3):
                arr[index+i] -= a

            cost += a*7

    '''
    while arr[index] != 0 and arr[index+1] != 0 and arr[index+2] != 0:
        arr[index] -= 1
        arr[index+1] -= 1
        arr[index+2] -= 1
        cost += 7
    '''

def two(arr, index, a):
    global cost
    if arr[index] != 0 and arr[index + 1] != 0:
        for i in range(2):
            arr[index + i] -= a
        cost += a * 5

    '''
    while arr[index] != 0 and arr[index+1] != 0:
        arr[index] -= 1
        arr[index+1] -= 1
        cost += 5
    '''



def one(arr, index):
    global cost
    if arr[index] != 0:
        a = arr[index]
        arr[index] -= a
        cost += a * 3

    '''
    while arr[index] != 0:
        arr[index] -= 1
        cost += 3
    '''


# 파이썬 최소값?
import sys

cost = 0
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n-2):
    if arr[i+1] > arr[i+2]:
        a = min(arr[i], arr[i+1] - arr[i+2])
        two(arr, i, a)
        three(arr, i)
    else:
        a = min(arr[i], arr[i+1])
        three(arr, i)
        two(arr, i, a)

    one(arr, i)


two(arr, n-2, min(arr[n-2], arr[n-1]))
one(arr, n-2)
one(arr, n-1)

print(cost)
