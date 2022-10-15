n = int(input())
m = int(input())

arr = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [0 for i in range(n+1)]
answer=[]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def bfs():
    queue=[1]
    visited[1]=1

    while queue:
        v=queue.pop(0)
        answer.append(v)
        for i in range(1, n+1):
            if (arr[v][i]==1 and visited[i]==0):
                queue.append(i)
                visited[i]=1
                
    print(len(answer)-1)

bfs()