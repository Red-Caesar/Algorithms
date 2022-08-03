s = "a"
letter_dict = dict()
for c in s:
    if c not in letter_dict:
        letter_dict[c] = 1
    else:
        letter_dict[c] += 1
cnt = 0
flag = False
for key, value in letter_dict.items():
    if value % 2 == 0:
        cnt += value
    else:
        flag = True
        cnt += value - 1
if flag:
    print(cnt + 1)
else:
    print(cnt)