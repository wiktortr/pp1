arr = [-15, 8, -31, 47, -2, 19]

# how dear you 
min_num = arr[0]
max_num = arr[0]
for x in arr:
    min_num = x if x < min_num else min_num
    max_num = x if x > max_num else max_num
print('min_num:', min_num)
print('max_num:', max_num)

