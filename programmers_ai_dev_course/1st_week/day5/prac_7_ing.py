class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 구현하세요
        pass

    def push(self, item):
        # 구현하세요
        pass

    def pop(self):
        # 구현하세요
        pass


# n, max_size = map(int, input().strip().split(' '))
# print(n, max_size)