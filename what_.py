def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계

    m = re.compile('[a-z0-9_\.-]')
    cnt = 0

    for i in range(len(new_id)):
        if i > len(new_id)-1:
            break
        else:
            if m.match(new_id[i]):
                continue
            else:
                # print(new_id[i],' unmatched')
                new_id = new_id.replace(new_id[i], '#') # 2단계
                cnt += 1

    # print('cnt: ', cnt)

    if '#' in new_id:
        # print('there is #')
        new_id = new_id.replace('#', '', cnt)
        # print(new_id)

    while '..' in new_id:
        new_id = new_id.replace('..', '.') # 3단계
        # print('3: ', new_id)

    if new_id != '' and new_id[0] == '.':
        new_id = new_id.replace('.', '',1)
        # print(new_id)

    if new_id != '' and new_id[len(new_id)-1] == '.':
        if len(new_id) <= 1:
            new_id = ''
        else:
            new_id = new_id[:len(new_id)-1] # 4단계
        # print('4: ',new_id)

    if new_id=='':
        new_id = 'a' # 5단계
        # print('5: ', new_id)

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[len(new_id) - 1] == '.':
            new_id = new_id[:len(new_id)-1] # 6단계
        # print('6: ', new_id)

    if len(new_id) <= 2:
        while True:
            new_id += new_id[len(new_id)-1]  # 7단계
            if len(new_id) == 3: break
        # print('7: ', new_id)

    answer = new_id

    return answer

import re


print('answer: ', solution('abcdefghijklmn.p'))
