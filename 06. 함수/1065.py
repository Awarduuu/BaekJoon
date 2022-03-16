# 입력
N = int(input())

# 한수인지 판별하는 함수
def hansu(n : int) :
    k = 0
    arr = []
    # 각 자리수 배열에 넣기
    for i in str(n):
        arr.append(int(i))
    
    # 세 자리부터 알고리즘 적용
    if len(arr) > 2 :
        # 공차 a 
        a = arr[1] - arr[0]
        # 반복문
        for i in range(len(arr)-1) :
            # 각 자리 수가 공차와 같다면 k += 1
            if arr[i+1] - arr[i] == a :
                k += 1
        # k가 자리수-1이면 각 자리 수가 등차수열이므로 한수
        if k == len(arr)-1 :
            return 1
        else : 
            return 0 
    # 두자리 수까지는 모두 한수
    else :
        return 1

cnt = 0

# 브루트포스 알고리즘
for i in range(1,N+1) :
    if hansu(i) == 1 :
        cnt += 1

print(cnt)
