# 이진 탐색 소스코드 구현 (재귀함수)
def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else :
        return binary_search(array, target, mid+1 , end)


# 이진 탐색 소스코드 구현 (반복문)
def binary_search_2(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid-1
        else:
            start = mid+1
    return None
    
# n(원소의 개수)과 target
n, target = map(int, input().split())

# 전체 원소
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None :
    print('원소가 존재하지 않습니다')
else :
    print(result + 1)

from bisect import bisect_left, bisect_right
# bisect_left(a, x) : 정렬된 순서의 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
# bisect_right(a, x) : 정렬된 순서의 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4

# 값이 특정 범위에 속하는 데이터 개수 구하는 함수
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 b 선언
b = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(b, 4, 4)) # 2

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(b, -1, 3)) # 6