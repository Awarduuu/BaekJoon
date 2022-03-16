cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
S = input()
sum = 0

for i in cro :
    if i in S :
        S = S.replace(i,"_")

cnt = S.count("_")
S_n = S.replace("_","")
sum = cnt + len(S_n)

print(sum)