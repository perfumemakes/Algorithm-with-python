def solution(keyinput, board):
    cor = [0,0]
    
    for i in keyinput:
        if i == "left":
            if cor[0] > -(board[0]-1)/2:
                cor[0] -=1
        elif i == "right":
            if cor[0] < (board[0]-1)/2:
                cor[0]+=1
        elif i == "up":
            if cor[1] < (board[1] -1)/2:
                cor[1]+=1
        else:
            if cor[1] > -(board[1]-1)/2:
                cor[1]-=1
    answer = cor
    return answer