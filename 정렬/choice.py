# 선택정렬
## 처리되지 않은 데이터 중 가장 작은 데이터와 가장 앞의 데이터의 위치를 바꾸는 알고리즘

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 전역 탐색
for i in range(len(arr)):
    # 비교대상 위치의 인덱스를 min_index로 설정
    min_index = i
    # 처리되지 않은 데이터를 비교
    for j in range(i+1, len(arr)):
        # 가장 작은 값의 인덱스 찾기
        if arr[min_index]>arr[j]:
            min_index = j
    # 비교대상 위치 데이터 값과 가장 작은 데이터 값 위치 스와이핑
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)