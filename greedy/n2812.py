
# 앞에서부터 k+1자리까지의 숫자중 가장 큰 숫자 남기고 삭제
# 그 뒷수자부터도 똑같이 반복

def delete(input, count, i):
    if count < 1:
        return input
    a = input[:count+1]
    index = a.index(max(a))
    if index < i:
        a = input[i:count+i+1]
        index = a.index(max(a))

    answer += 1
    count -= (index)
    print(index)
    print(count)
    input = input[index:]
    i += 1


    return delete(input, count, i)

n, k = map(int, input().split())
num = input()
score = 0
ahswer = ''
delete(num, k, score)

print(answer)
