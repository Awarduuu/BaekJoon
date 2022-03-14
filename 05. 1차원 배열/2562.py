from operator import indexOf
arr = []

for i in range(9) :
    arr.append(int(input()))

k = max(arr)

ind = indexOf(arr,k) +1

print(k)
print(ind)