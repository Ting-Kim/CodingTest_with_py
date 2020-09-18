# 백준 1260번

def dfs(graph, v, visited):  # Stack 기반
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):  # Queue 기반
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

from collections import deque

answer1 = []
answer2 = []
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

visited1 = [False for i in range(len(graph))]
visited2 = [False for i in range(len(graph))]
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)

