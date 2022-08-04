s = "("
open_stack = []
close_stack = []
ans = False
for p in s:
    if p == '(' or p == '[' or p == '{':
        open_stack.append(p)
    else:
        close_stack.append(p)
        if p == ')' and open_stack and open_stack[len(open_stack) - 1] == '(':
            open_stack.pop()
            close_stack.pop()
        if p == ']' and open_stack and open_stack[len(open_stack) - 1] == '[':
            open_stack.pop()
            close_stack.pop()
        if p == '}' and open_stack and open_stack[len(open_stack) - 1] == '{':
            open_stack.pop()
            close_stack.pop()

if len(open_stack) == 0 and len(close_stack) == 0:
    ans = True
print(ans)
