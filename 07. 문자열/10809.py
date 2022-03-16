from operator import indexOf
# 입력
S = input()

# 알파벳
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp :
    if i in S :
        print(indexOf(S, i), end = ' ')
    else :
        print(-1, end = ' ')

# find 함수 이용

# for i in alp :
#     print(S.find(i), end=' ')