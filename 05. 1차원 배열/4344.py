N = int(input())

for i in range(N) :
    k = 0
    arr = list(map(int, input().split()))
    mean_sc = (sum(arr) - arr[0])/(arr[0])
    for i in range(1, arr[0]+1) :
        if arr[i] > mean_sc :
            k += 1
    perc = (k / arr[0]) * 100
    print('{:.3f}%'.format(perc))
    