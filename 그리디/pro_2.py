S = input()
# 시작점을 설정하는 법!
result = int(S[0])

for i in range(1,len(S)) :
    num = int(S[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num
print(result)