def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    
    for i in graph(v):
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    from collections import deque
    
    queue=deque([start])
    visited[start]=True
    
    while(queue):
        v = deque.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[v]:
                visited[v]=True
                queue.append(i)
    
    