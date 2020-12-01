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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens

'''구현 필요'''
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for element in tokenList:
        if element in prec:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[element] and element != '(':
                postfixList.append(opStack.pop())
            opStack.push(element)
        else:
            if element == ')':
                while not opStack.isEmpty():
                    if opStack.peek() == '(':
                        opStack.pop()
                        break
                    postfixList.append(opStack.pop())
            else:
                postfixList.append(element)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    # tokenList = [1, 2, '+', 3, 4, '+']
    temp1 = 0
    temp2 = 0
    opStack = ArrayStack()
    for element in tokenList:
        if element == '+':
            temp2 = opStack.pop()
            temp1 = opStack.pop()
            opStack.push(temp1+temp2)

        elif element == '-':
            temp2 = opStack.pop()
            temp1 = opStack.pop()
            opStack.push(temp1-temp2)

        elif element == '/':
            temp2 = opStack.pop()
            temp1 = opStack.pop()
            opStack.push(temp1/temp2)

        elif element == '*':
            temp2 = opStack.pop()
            temp1 = opStack.pop()
            opStack.push(temp1*temp2)

        else:
            opStack.push(element)

    if opStack.size() == 1:
        return opStack.pop()
    else:
        return -1

def solution(expr):
    tokens = splitTokens(expr)
    print(tokens)
    postfix = infixToPostfix(tokens)
    print(postfix)
    val = postfixEval(postfix)
    return val

expr = '(1+2)*(3+4)'
print(solution(expr))