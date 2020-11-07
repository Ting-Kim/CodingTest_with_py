def solution(penter, pexit, pescape, data):
    arr_data = list(data)
    length = len(penter)
    temp = 0
    for i in range(0, len(data)-1, length):
        a = data[i:i+length]
        if a == penter or a == pexit or a == pescape:
            print(a)
            arr_data.insert(i+temp, pescape)
            print(arr_data)
            temp += 1

    # 마지막
    arr_data.insert(0, penter)
    arr_data.append(pexit)

    return ''.join(arr_data)

penter = "10"
pexit = "11"
pescape = "00"
data = "00011011"
print(solution(penter, pexit,pescape,data))