# 입력
H, M = map(int, input().split())

# 조건문
if H != 0 :
    if M < 45 :
        print(H-1, M+15)
    else :
        print(H, M-45)
else :
    if M < 45 :
        print(H+23, M+15)
    else :
        print(H, M-45)