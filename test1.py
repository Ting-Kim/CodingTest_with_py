import re
new_id = '.w>e1!2w1qqqqqqqqqqqqqqq3jq2..sw+qeqqqqqqq.'
# print(new_id[len(new_id)-1])
m = re.compile('[a-z0-9\-_.]')

for i in range(len(new_id)):
    if i > len(new_id) - 1:
        break
    else:
        if m.match(new_id[i]):
            continue
        else:
            new_id = new_id.replace(new_id[i], '')  # 2단계
if len(new_id) >= 16:
    new_id = new_id[:15]

print(new_id)