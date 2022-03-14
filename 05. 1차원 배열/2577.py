# 숫자 입력 받기
arr = []
for i in range(3) :
    arr.append(int(input()))

# 세 수 의 곱
num = arr[0] * arr[1] * arr[2]
# string 변환
num = str(num)

# index 초기값
N = 0

# 이중 for문으로 구성
for i in range(10) :
    # 0~9까지 loop
    for j in num:
        # num의 각 자리수
       if str(i) == j :
           # 0부터 자리수와 같으면 N 1 증가
           N+=1
    print(N)    
    # N reset
    N = 0



