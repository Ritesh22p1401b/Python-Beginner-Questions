n = 6
arr = [9, 8, 3, 6, 2, 0]
for i in range(1, n):
    j = i - 1
    temp = arr[i]
    while arr[j] > temp and j >= 0:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = temp
print(arr)
