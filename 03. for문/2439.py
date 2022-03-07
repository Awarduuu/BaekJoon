n = int(input())

for i in range(1,n+1) :
    k = '*'*i
    print("{0:>{1}s}".format(k,n))