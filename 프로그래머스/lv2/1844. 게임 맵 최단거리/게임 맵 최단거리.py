def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    queue = []
    queue.append([0,0])
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
    print(maps)
    return -1 if maps[-1][-1] == 1 else maps[-1][-1]