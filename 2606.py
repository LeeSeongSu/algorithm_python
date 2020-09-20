count = 0
def dfs(v):
    global count
    count += 1

    visited[v] = True
    for i in graph[v]:
        if not(visited[i]):
            dfs(i)



n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
dfs(1)
print(count-1)