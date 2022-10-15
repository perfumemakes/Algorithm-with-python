n, m, v = map(int, input().split())
arr = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


def dfs(v):
    visited[v] = 1
    print(v, end = ' ')

    for i in range(1,n+1):
        if (arr[v][i]==1 and visited[i]==0):
            dfs(i)

def bfs(v):
    queue=[v]
    visited[v]=0

    while queue:
        v=queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if (arr[v][i]==1 and visited[i]==1):
                queue.append(i)
                visited[i]=0
dfs(v)
print()
bfs(v)