# Recursive
def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x-1) + solution(x-2)

# Iterative
def solution1(x):
    f0 = 0
    f1 = 1

    if x == 1:
        return 0
    elif x == 1:
        return 1

    for i in range(2, x+1):
        fn = f1 + f0
        f0 = f1
        f1 = fn


    return fn

x = 6
print(solution(x))