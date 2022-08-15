# s = "3[a]2[bc]"
# s = "3[a2[c]]"
# "accaccacc"
s = "2[abc]3[cd]ef"
stack = []
id = 0
num = ''
while id != len(s):
    if s[id].isdigit():
        num += s[id]
    elif s[id].isalpha():
        stack.append(s[id])
    elif s[id] == '[':
        stack.append(int(num))
        stack.append(s[id])
        num = ''
    elif s[id] == ']':
        el = ''
        n_s = ''
        while el != '[':
            n_s = el + n_s
            el = stack.pop()
        n_s = n_s*stack.pop()
        stack.append(n_s)
    id += 1

print(''.join(stack))