# while 무한루프
while True :
    A, B = map(int, input().split())

    # 조건식으로 while문 강제 종료
    if A == 0 and B == 0 :
        break
    else :
        C = A + B
        print(C)