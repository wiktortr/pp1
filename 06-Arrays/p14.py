arr = [[True,False],[True,True],[False,False]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = not arr[i][j]
print(arr)