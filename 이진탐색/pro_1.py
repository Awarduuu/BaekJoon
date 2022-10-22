# 떡의 개수(N)와 요청한 떡의 길이(m)을 입력
n, m = map(int, input().split())

# 떡의 개별 높이 입력
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 결과값을 저장할 변수
result = 0

# 이진탐색 수행 (반복문)
while(start<=end) :
    total = 0
    mid = (start+end) // 2
    # 떡을 잘랐을 때 총 떡의 양 계산
    for x in array:
        if x > mid :
            total += x - mid
    # 총 양이 m 보다 작으면 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m :
        end = mid - 1
    # 총 양이 m보다 크거나 같으면 덜 자르기 (오른쪽 부분 탐색)
    else : 
        result = mid
        start = mid + 1

print(result)