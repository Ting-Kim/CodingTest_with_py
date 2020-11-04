def solution(number, k):
    numbers = [element for element in number] # 이게 더 빠름..
    # numbers = list(map(str, number))
    # while k > 0:
    #     if k >= len(number):
    #         return answer
    a = 0
    for i in range(k):
        idx = len(numbers) - 1

        for j in range(idx):
            if numbers[j] == '9':
                continue
            if numbers[j+1] == '0':
                idx = j+1
                break
            if numbers[j] < numbers[j+1]:
                idx = j
                break

        print(numbers.pop(idx))

    # for element in numbers:     # 이게 더 빠름
    #     answer += element
    return ''.join(numbers)

number = "4177252841"
k = 4
print(solution(number,k))