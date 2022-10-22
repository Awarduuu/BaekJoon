from collections import deque

# bfs 함수 작성
def bfs(x,y):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque()
    # 큐에 첫 좌표 넣기 
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue :
        # 첫 좌표를 큐에서 빼 변수값에 넣기
        x, y = queue.popleft()
        # 현재 방향에서 상, 하, 좌, 우 4방향으로 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 위치가 범위 밖이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            # 만약 위치값이 0인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 만약 위치 값이 1인 경우(처음방문하는 경우) 최단거리 기록
            if graph[nx][ny] == 1:
                # 이동할 위치의 값에 1 추가
                graph[nx][ny] = graph[x][y] + 1
                # 이동할 위치값을 큐에 삽입
                queue.append((nx,ny))
    # 가장 오른쪽 하단까지의 최단 거리 반환            
    return graph[n-1][m-1]


n, m = map(int, input().split())

graph = []

for i in range(n) :
    graph.append(list(map(int,input())))

# 방향벡터
# x축은 상하(row이기 때문)
dx = [-1, 1, 0, 0]
# y축은 좌우(col이기 때문)
dy = [0, 0, -1, 1]

print(bfs(0,0))