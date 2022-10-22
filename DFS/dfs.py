# DFS 알고리즘
# 스택 자료구조(혹은 재귀함수)이용
# 깊은 부분을 우선적으로 탐색하는 알고리즘
# DFS 메서드 정의
def dfs(graph, v, visited) :
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited) 