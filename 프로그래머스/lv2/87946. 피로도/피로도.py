def solution(k, dungeons):
    cnt = []
    visited=[0]*len(dungeons)
    
    def dfs(k, dungeons, num):
        if not 0 in visited:
            cnt.append(num)
            return
        
        for i in range(len(dungeons)):
            if visited[i] == 0:
                x, y = dungeons[i]
                visited[i] = 1
                if k>=x:
                    k-=y
                    dfs(k, dungeons, num+1)
                    visited[i]=0
                    k+=y
                else:
                    dfs(k, dungeons, num)
                    visited[i]=0

                
    dfs(k,dungeons,0)
    answer = max(cnt)
    return answer