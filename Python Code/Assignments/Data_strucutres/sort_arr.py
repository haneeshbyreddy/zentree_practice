arr = [1,4,6,7,2,4,6,9,7,1,1,6,7,3,5,5,8,3]
print('input arr :', arr)

# sorting the array
for i in range(len(arr)):
    ptr = i
    while ptr>0 and arr[ptr-1] > arr[ptr]:
        arr[ptr-1], arr[ptr] = arr[ptr], arr[ptr-1]
        ptr -= 1
print('sorted arr', arr)

# remove duplicates
i = ptr = 0
while ptr<len(arr): 
    while arr[i] == arr[ptr]:
        ptr += 1
        if ptr >= len(arr):
            break
    if ptr<len(arr):
        arr[i+1] = arr[ptr]
    i+= 1
arr = arr[:i]

print('after removing duplicates', arr)
print(arr)