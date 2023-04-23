def DFS(v, graph, visited, check_link):
    cnt = 1
    visited[v] = True
    
    for adj_v in graph[v]:
        if visited[adj_v] == False and check_link[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check_link)
    
    return cnt

def solution(n, wires):
    answer = n
    check_link = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False]*(n+1)
        check_link[a][b] = False # a-b 간선 끊기
        cnt_a = DFS(a, graph, visited, check_link)
        cnt_b = DFS(b, graph, visited, check_link)
        check_link[a][b] = True # a-b 간선 다시 연결
        
        answer = min(answer, abs(cnt_a - cnt_b))
    
    return answer