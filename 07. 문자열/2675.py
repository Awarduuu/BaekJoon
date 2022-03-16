N = int(input())

for i in range(N) :
    # R, S 입력
    R, S = input().split()
    # R 정수형으로 변환
    R = int(R)
    # 새로운 문자 P 선언
    P = ''

    # P 만들기
    for j in S :
        P += j*R
    # P 출력
    print(P)