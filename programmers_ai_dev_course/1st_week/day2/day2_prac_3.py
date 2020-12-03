def solution(numbers):
    # answer = []
    # numbers_to_string = []
    # for element in numbers:
    #     numbers_to_string.append((str(element), (str(element)*3)[:3]))

    # numbers_to_string.sort(key=lambda x:x[1], reverse=True)
    numbers_string = list(map(str, numbers))
    numbers_string.sort(key=lambda x: str(x)*3, reverse=True)
    return str(int(''.join(numbers_string)))
    # print(numbers_to_string)
    # for element,key in numbers_to_string:
    #     answer.append(element)
    # print(answer)
    # answer_to_string = str(int(''.join(answer)))
    # return answer_to_string

numbers = [3, 30, 34, 5, 9, 100, 1000, 202, 20, 101, 10]
print(solution(numbers))
