n = int(input())
arr = list(map(int, input().split()))


def possible(num):
    for i in range(1, len(num)):
        if num[i-1] > num[i]:
            return False
    return True


if possible(arr):
    n_set = list(set(arr))
    cnt = 0
    for i in range(1, len(n_set)):
        cnt += (n_set[i] - n_set[i-1])
    print(cnt)
else:
    print(-1)