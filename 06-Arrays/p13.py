arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum_of_even = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum_of_even += arr[i][j] if arr[i][j] % 2 == 0 else 0
print('sum_of_even:', sum_of_even)
