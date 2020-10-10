n, l = map(int, input().split())
# arr = ['.' for _ in range(1000000001)]
index = []
answer = 0
for _ in range(n):
    water = list(map(int, input().split()))
    index.append(water)

index.sort(key=lambda x:x[0])
# print(index)
# 다시 새로운 풀이로 풀어보기..
i = 0   # 체크할 길 index

for element in index:
    start = element[0]
    end = element[1]-1

    if i < start:
        i = start

    # 시간 초과로 인한 수정
    sum =  end - i
    namu = (sum // l) + 1
    # print("i = %d" % i)
    # print("namu = %d" % namu)
    i += l*(namu)
    answer += namu


    # while i <= end:
    #     # print('i = %d' % i)
    #     i += l
    #     answer += 1
    #     # 다음 element로

print(answer)


'''
5 3
1 5
6 7
9 13
12 14
19 22

5
'''