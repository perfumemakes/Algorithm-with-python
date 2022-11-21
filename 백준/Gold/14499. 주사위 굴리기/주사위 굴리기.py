import sys

input = sys.stdin.readline

N,M,x,y,o=map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dir = list(map(int, input().split()))
dice = [0,0,0,0,0,0,0]
answer = []

def roll(dir):
    global arr, dice, answer, x, y
    temp = [0]
    
    if dir==1:
        y+=1
        if 0<=y<M:
            temp.append(dice[3])
            temp.append(dice[2])
            temp.append(dice[6])
            temp.append(dice[1])
            temp.append(dice[5])
            temp.append(dice[4])
            if arr[x][y] != 0:
                temp[1] = arr[x][y]
                arr[x][y] = 0
            else:
                arr[x][y] = temp[1]
                
        else:
            y-=1
            return

    if dir== 2:
        y-=1
        if 0<=y<M:
            temp.append(dice[4])
            temp.append(dice[2])
            temp.append(dice[1])
            temp.append(dice[6])
            temp.append(dice[5])
            temp.append(dice[3])
            if arr[x][y] != 0:
                temp[1] = arr[x][y]
                arr[x][y] = 0
            else:
                arr[x][y] = temp[1]
            
        else:
            y+=1
            return
        
    if dir==3:
        x-=1
        if 0<=x<N:
            temp.append(dice[2])
            temp.append(dice[6])
            temp.append(dice[3])
            temp.append(dice[4])
            temp.append(dice[1])
            temp.append(dice[5])
            if arr[x][y] != 0:
                temp[1] = arr[x][y]
                arr[x][y] = 0
            else:
                arr[x][y] = temp[1]
            
        else:
            x+=1
            return
    
    if dir==4:
        x+=1
        if 0<=x<N:
            temp.append(dice[5])
            temp.append(dice[1])
            temp.append(dice[3])
            temp.append(dice[4])
            temp.append(dice[6])
            temp.append(dice[2])
            if arr[x][y] != 0:
                temp[1] = arr[x][y]
                arr[x][y] = 0
            else:
                arr[x][y] = temp[1]
            
        else:
            x-=1
            return    
    dice=temp
    answer.append(dice[6])
    
for i in range(o):
    roll(dir[i])

for i in answer:
    print(i)