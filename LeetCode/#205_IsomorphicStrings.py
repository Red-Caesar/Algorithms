s = "paper"
t = "title"
hash_t = dict()
for i in range(len(t)):
    if t[i] not in hash_t.keys():
        hash_t[t[i]] = s[i]
    elif hash_t[t[i]] == s[i]:
        continue
    else:
        print(False)
        break
if len(set(hash_t.values())) == len(hash_t.values()):
    print(True)
else:
    print(False)

