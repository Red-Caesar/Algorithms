# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(4))

n = 0
a, b = 0, 1
while n > 1:
    a, b = b, a+b
    n -= 1
if n == 0:
    print(a)
else:
    print(b)


