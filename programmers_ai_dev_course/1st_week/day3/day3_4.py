def solution(number, k):
    number_list = list(map(str, number))
    arr = []
    # print(number_list)
    # Greedy(탐욕법)
    # number 에서 하나씩 꺼내면서 리스트에 담고,
    # 리스트가 비어있지 않다면 마지막 인덱스에 있는 원소와 비교하여
    # 꺼낸 원소가 더 큰 경우, k가 남아있는 한에서 리스트의 원소를 pop한다
    for i, num in enumerate(number_list):

        while k > 0 and arr and arr[-1] < num:
            arr.pop()
            k -= 1

        if k == 0:
            arr += number_list[i:]
            break
        arr.append(num)

    answer = ''.join(arr[:-k]) if k > 0 else ''.join(arr)

    return answer

number = "4177252841"
k = 4
print(solution(number,k))