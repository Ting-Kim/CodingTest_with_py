def solution(s, op):
    answer = []

    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])
        if op == "*":
            answer.append(a*b)
        elif op == "+":
            answer.append(a+b)
        elif op == "-":
            answer.append(a-b)
        else:
            print("조건에 있는 연산자가 아닙니다.")

    return answer


s = "31402"
op = "*"
print(solution(s,op))