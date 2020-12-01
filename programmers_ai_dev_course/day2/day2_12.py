class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = []

    for element in S:
        # [+, -, *, /, (] 중 하나라면
        if element in prec:
            # Stack이 비어있지 않으면서 element가 괄호가 아닐 때
            # 즉, 연산 기호일 때
            while not opStack.isEmpty() and element != '(' and prec[opStack.peek()] >= prec[element]:
                # Stack 가장 윗값이 element 보다 우선순위가 높으면 pop해서 answer에 이어붙이기
                answer.append(opStack.pop())
                # while prec[opStack.peek()] >= prec[element]:
                #     answer.append(opStack.pop())

            # element는 [+, -, *, /, (] 중 하나라면 모든 경우에 결국 Stack에 push
            opStack.push(element)

        # [+, -, *, /, (] 이외의 경우
        else:
            # 닫는 괄호의 경우 열린 괄호가 나올 때까지 Stack에서 pop()
            if element == ')':
                while not opStack.isEmpty():
                    if opStack.peek() == '(':
                        opStack.pop()
                        break
                    answer.append(opStack.pop())

            # 알파벳인 경우 바로 answer에 붙임
            else:
                answer.append(element)

    # Stack 비우기
    while not opStack.isEmpty():
        answer.append(opStack.pop())

    return ''.join(answer)

print(solution('A+B*C+D'))

