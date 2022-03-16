S = input()

min = 0

# 방법 1

# if문 하나로 진행
# for i in S :
#     min += 1
#     if i in 'ABC' :
#         min +=2
#     elif i in 'DEF' :
#         min +=3
#     elif i in 'GHI' :
#         min +=4
#     elif i in 'JKL' :
#         min +=5
#     elif i in 'MNO' :
#         min += 6
#     elif i in 'PQRS' :
#         min += 7
#     elif i in 'TUV' :
#         min += 8
#     else :
#         min += 9

# print(min)

# 방법 2
# 리스트로 쪼개서 이중 FOR문
alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in S :
    min+=1
    for d in alp :
        if i in d :
            min = min + alp.index(d) + 2

print(min)