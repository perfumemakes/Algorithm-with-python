def recursive(node, computers, visited)->list:
    visited[node] = 1
    for i, v in enumerate(computers[node]):
        if i==node: continue
        
        if v != 0 and visited[i]==0:
            recursive(i, computers, visited)
        
    return visited
    
def solution(n, computers)->int:
    
    answer = 1
    visited = [0]*n
    node = 0
    
    
    while True:
        visited = recursive(node, computers, visited)
        if 0 in visited:
            answer +=1
            node = visited.index(0)
            recursive(node, computers, visited)
        else:
            break
    
    return answer