from operator import indexOf

S = input()

# 대문자로 변환
S = S.upper()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

arr = []

for i in alp :
    cnt = 0
    for j in S :
        if i == j :
            cnt += 1
    arr.append(cnt)

index = indexOf(arr, max(arr))

# (point) count 함수를 활용하여 max 값을 가진 객체 개수 구하기
if arr.count(max(arr)) > 1 :
    print('?')
else :
    print(alp[index])