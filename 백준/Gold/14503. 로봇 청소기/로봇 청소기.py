import sys
input = sys.stdin.readline

N,M = map(int, (input().split()))
x,y,d=map(int,(input().split()))
map=[list(map(int,input().split())) for _ in range(N)]
visited = [ [0]*M for _ in range(N) ]
visited[x][y]=1
dir = [[-1,0], [0,1], [1,0], [0,-1]]
new_x, new_y = dir[d]
cnt = 1

while True:
    check = 0
    for _ in range(4):
        d = (d+3)%4
        new_x, new_y = x+dir[d][0], y+dir[d][1]
        
        if 0<=new_x<N and 0<=new_y<M and map[new_x][new_y]==0:
            if visited[new_x][new_y] == 0:
                visited[new_x][new_y]=1
                cnt += 1
                x = new_x
                y = new_y
                check = 1
                break
    if check == 0:
        if map[x-dir[d][0]][y-dir[d][1]] == 1:
            print(cnt)
            break
        else:
            x,y = x-dir[d][0], y-dir[d][1]