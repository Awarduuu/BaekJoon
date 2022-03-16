N = int(input())
a = []
for i in range(N):
    a.append(input())
b = []
c = []

cnt_r = 0
for i in a :
    cnt = 0
    b = []
    for j in range(len(i)) :
        if i[j] not in b :
            b.append(i[j])
        else :
            if i[j] == b[j-1] :
                b.append(i[j])
            else :
                b.append(i[j])
                cnt +=1
    c.append(cnt)

for i in c :
    if i == 0 :
        cnt_r+=1

print(cnt_r)