s = "3z4"
arr = []

def rec(i, n_s):
    if i == len(s):
        arr.append(n_s)
        return
    if not s[i].isdigit():
        rec(i + 1, n_s + s[i])
        if s[i].islower():
            rec(i + 1, n_s + s[i].upper())
        else:
            rec(i + 1, n_s + s[i].lower())
    else:
        rec(i+1, n_s+s[i])


rec(0, '')
print(arr)