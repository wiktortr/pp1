arr = [[2,5,4],[9,0,3]]
print(arr)
print(len(arr), len(arr[0]))
print(arr[0][1])
print(arr[1][2])
print(arr[1])
for i in range(len(arr)):
    print(' '.join([str(x) for x in arr[i]]))
for i in range(len(arr)):
    print(arr[i][-1])