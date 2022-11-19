arr = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(arr)):
    arr[i][i] = 1
    print(' '.join([str(x) for x in arr[i]]))
    