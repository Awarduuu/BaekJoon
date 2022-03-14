from statistics import mean
# 정수 개수 입력
N = int(input())

# list에 점수 입력
score = list(map(int, input().split()))

# 최대값
max_sc = max(score)

# 새로운 배열 생성
re_sc =[]

# 새로운 배열에 수정된 값들 append
for i in range(N) :
    re_sc.append(score[i]/max_sc*100)

# 새로운 평균
mean_sc = mean(re_sc)
print(mean_sc)