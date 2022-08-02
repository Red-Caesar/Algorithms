n = 2
arr = [1 for _ in range(n)]
for i in range(n):
    if (i-2) >= 0:
        arr[i] = arr[i-2] + arr[i-1]
    elif (i-2) == -1:
        arr[i] += 1

print(arr[n-1])
