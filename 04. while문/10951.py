# try except으로 오류가 생길 시 무한루프 강제종료
while True :
    try :
        A, B = map(int, input().split())
        C = A+B
        print(C)
    except :
        break

# 방법 2
# try except문 안에 while문 작성
# 런타임이 사소한 차이로 우위
try :
    while True :
        A, B = map(int, input().split())
        C = A+B
        print(C)
except :
    exit()