


a = input()     # 문서
b = input()     # 찾으려는 단어

l = list(map(str, a.split(b)))
# 답 : 스플릿한 결과 element 갯수 - 1
answer = len(l) - 1

# print(b in a)

print(answer)