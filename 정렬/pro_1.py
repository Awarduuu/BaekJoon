N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 배열 A는 오름차순 정렬 수행
B.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

for i in range(K): # 최대 K번 비교
    if A[i] < B[i] : # A의 원소가 B의 원소보다 작을경우
        A[i], B[i] = B[i], A[i] # 스와핑
    else : # 그렇지 않을 경우, 더 이상 만족하는 답을 찾을 수 없으므로 반복문 탈출
        break

# 정답 출력
print(sum(A))
