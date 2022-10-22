# 정수 N을 입력 받기
n = int(input())

# 식량 창고 정보 입력 받기
array = list(map(int, input().split()))

# 결과를 저장하기 위한 dp 테이블
d = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])

# idea
# 두가지 경우만 고려하면 됨
# i번째 창고를 합치는 경우 -> i-2번째 결과값만 알면됨
# i번째 창고를 합치지 않는 경우 -> i-1번째 결과값만 알면 됨
# 이 두 가지 경우를 비교하여 큰 값을 i번째 결과로 채택함
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

# 계산된 결과 출력
print(d[n-1])