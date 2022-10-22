N = int(input())
data = list(input().split())

x, y = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# !!! 첫번째 idea !!!
# move_types이라는 주어진 문자열과 방향벡터를 같은 위치의 벡터로 일치시키는 행위
move_types = ['L', 'R', 'U', 'D']

# 브루트포스 방식으로 모든 입력값에 대해 반복문 시행
for i in data :
    # 한단계씩 movetype과 비교
    for j in range(len(move_types)):
        # 무브타입과 일치하는 단계라면 
        if i == move_types[j]:
            # 방향벡터 이동
            nx = x + dx[j]
            ny = y + dy[j]

    # !!! 두번째 idea !!!
    # 무시해도 되는 경우는 continue문을 통해 진행하기
    if nx < 1 or ny < 1  or nx > N or ny > N :
        continue
    x, y = nx, ny

print(x, y)



    
    
    
