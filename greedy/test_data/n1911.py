n, l = map(int, input().split())
# arr = ['.' for _ in range(1000000001)]
index = []
answer = 0
for _ in range(n):
    water = list(map(int, input().split()))
    index.append(water)

index.sort(key=lambda x:x[0])

# 다시 새로운 풀이로 풀어보기..









# i = 0
# while i < n-1:
#     length = index[i][1] - index[i][0]
#     # 일반적인 독립적인 경우
#     if index[i+1][0] - index[i][1] > l - (length % l) or length % l == 0:
#         if length % l == 0:
#             answer += length // l
#         else:
#             answer += length // l + 1
#
#         i += 1
#     else:
#         j = i
#         while index[i+1][0] - index[i][1] <= l - (length % l) and length % l != 0:
#             start = index[j][0]
#             end = index[i][1]
#             length = (end-start)
#             i += 1
#             if i >= n-1:
#                 break
#
#         i -= 1
#
#         if length % l == 0:
#             answer += length // l
#             # i += 1
#         else:
#             answer += length // l + 1
#             # i += 1

# print(index)
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