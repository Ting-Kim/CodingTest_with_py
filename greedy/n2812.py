
# 앞에서부터 k+1자리까지의 숫자중 가장 큰 숫자 남기고 삭제
# 그 뒷수자부터도 똑같이 반복
# 재귀.. 메모리 초과


def delete(input, count):
    answer = ''
    if count < 1:
        return answer

    # a = input[:count+1]
    MNum = max(input[:count+1])
    index = input[:count+1].index(MNum)

    count -= (index)
    # print(count)
    # print(index)
    answer += MNum
    input = input[index+1:]

    return delete(input, count, answer)

n, k = map(int, input().split())
num = input()
delete(num, k)

print(answer)
