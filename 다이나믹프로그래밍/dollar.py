# 정수 N, M을 입력 받기
N, M = map(int, input().split())

# N개의 화폐 단위 정보 입력 받기
array = []
for i in range(N) :
    array.append(int(input()))

# dp 테이블 초기화
d = [10001] * (M+1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
# N개 화폐단위 반복문
for i in range(N) : 
    # 금액 반복문
    for j in range(array[i], M+1) :
        if d[j-array[i]] != 10001 : # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1) # 기존 방법과 (i-k)원을 만드는 방법 + 1을 비교하여 최소인 값으로 갱신

if d[M] == 10001 :
    print(-1)
else :
    print(d[M])