arr = [1,2,3,4,5]
print(arr)
arr[0] -= 1
print(arr)
arr[-1] += 4
print(arr)
arr[len(arr) // 2] *= 2
print(arr)
arr = [x + 3 for x in arr]
print(arr)