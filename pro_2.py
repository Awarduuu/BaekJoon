arr = [1,2,3,1,1,1]

for i in range(0,len(arr)) :
    for j in range(i, len(arr)+1):
        slice = arr[i:j]
        print(slice)

