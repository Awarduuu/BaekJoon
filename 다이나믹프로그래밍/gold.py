# 테스트 케이스 입력
for tc in range(int(input())) :
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0

    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    ## index를 이용하여 slicing하는 IDEA!
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # 다이나믹 프로그래밍 진행 (보텀업)
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0 : left_up = 0
            else : left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1 : left_down = 0
            else : left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # 점화식
            # 현재 위치 갱신은 '현재 + 왼쪽 위, 아래, 정공법 중 최대값'
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)