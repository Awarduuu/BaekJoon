# 퀵정렬
# 이상적인 경우 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
# 하지만 최악의 경우 O(N^2)의 시간복잡도를 가질 수 있다.(분할이 한쪽으로 쏠릴때)
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end : # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    # left와 right가 엇갈릴때까지 반복
    while(left <= right) :
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if(left > right) :
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else :
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)


def quick_sort_2(array) :
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

print(quick_sort_2(arr))
