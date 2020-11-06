def solution(number, k):
    answer = []
    numbers = [element for element in number]  # 이게 더 빠름..
    # numbers = list(map(str, number))
    # while k > 0:
    #     if k >= len(number):
    #         return answer
    idx = -1
    length = len(numbers)

    # mx = max(numbers)
    # pattern = re.compile('[0-'+str(int(mx)-1)+']')

    # print(mx)

    for i in range(length - k):
        # if pattern.search(''.join(numbers)) == None:
        #     return ''.join(numbers[:k-i])

        temp = '0'
        for j in range(idx+1, k+len(answer)+1): #

            if numbers[j] > temp:
                idx = j
                temp = numbers[j]
            if numbers[j] == '9':
                idx = j
                temp = numbers[j]
                break

        # answer.append(numbers[idx]) # => 루프에서 조건문 한번도 통과 못 했을 시 idx가 이전 루프값을 그대로 받아오는 문제..
        answer.append(temp)

    return ''.join(answer)


number = "12034506708"
k = 6
print(solution(number, k))

'''
980469200056510
988469222256511


56778
'''