from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not(visited[i]):
            dfs(i)

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in graph[v]:
                if not visited[e]:
                    queue.append(e)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)