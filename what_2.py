def solution(orders, course):
    answer = []
    com_list1 = []
    com_list2 = []
    menu = ''

    for i in range(len(orders)):
        menu += orders[i]

    menu = ''.join(sorted(set(menu)))
    # menu = ''.join([j for i,j in enumerate(menu) if j not in menu[:i]])
    print('ordered menes : ', menu)

    for j in range(2, len(menu)):
        com_list1 += list(combinations(menu, j))

    cnt = [0 for i in range(len(com_list1))]

    print(cnt)

    for i in range(len(com_list1)):
        for j in range(len(orders)):
            check = 0
            for k in range(len(com_list1[i])):
                if com_list1[i][k] in orders[j]:
                    check += 1
            if check == len(com_list1[i]):
                cnt[i] += 1

    print(com_list1)
    print(cnt)

    for element in course:
        for i in range(len(cnt)):
            if element == cnt[i]:
                word = ''
                for j in range(len(com_list1[i])):
                    word += com_list1[i][j]
                answer.append(word)



    #
    # for k in com_list1:
    #     element = ''
    #     for l in range(len(k)):
    #         element += k[l]
    #     com_list2.append(element)

    # for i in range(len(com_list2)):
    #     for j in range(len(orders)):
    #         if com_list2[i] in orders[j]:
    #             print(com_list2[i])
    #             if com_list2[i] in answer:
    #                 continue
    #



            # continue
        # if com_list2[i] in orders:
        #     continue
            # if comanswer
            # print(com_list2[i])
            # answer.append(com_list2[i])



    return answer

from itertools import combinations

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))
