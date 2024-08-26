from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력을 받아서 그래프를 구성하는 부분
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 기록용 리스트 생성
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# 방문 기록용 리스트 초기화 후 BFS 수행
visited = [False] * (n + 1)
bfs(graph, v, visited)
