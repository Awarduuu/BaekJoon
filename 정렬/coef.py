# 계수정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
## 조건 : 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr) + 1)

for i in range(len(arr)) :
    count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)) : # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]) :
        print(i, end='') # 띄어쓰기를 구분으로 등장한 횟수만큼 출력