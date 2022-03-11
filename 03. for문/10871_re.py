# n = 원소 개수, st = 기준값 입력
n, st = map(int, input().split())

# 리스트형태로 원소 n개 받기
l = list((map(int, input().split())))

# 결과값을 저장할 빈 리스트 생성
result = []

# 반복문
for i in range(n) :
    # 기준보다 작은 원소 조건
    if l[i] < st :
        # 결과 리스트에 저장
        result.append(l[i])


for i in range(len(result)) :
    
    # end 속성을 이용한 print
    print(result[i], end=' ')