def solution(board):
    #only for ex3.
    n = len(board)
    """cnt = 0
    for i in board:
        if len(set(i))==1:
            cnt+=1
            continue
        else:
            break
    if cnt == n:
        if board[0][0]==1:
            return 0
        else:
            return n*n   
        
    if cnt == n:
        return n*board[0][0]
    """
    #for general case
    
    cor = []
    for i in range(0, n):
        for v in range(0, n):
            if board[i][v] == 1:
                cor.append((i,v))
                
    for i in cor:
        flag1, flag2 = 0, 0
        if i[0] - 1 >= 0:
            flag1 = 1
            board[i[0]-1][i[1]] = 1
        if i[0] + 1 < n:
            flag2 = 1
            board[i[0]+1][i[1]] = 1
            
        if  i[1]-1 >= 0:
            board[i[0]][i[1]-1] =1
            if flag1:
                board[i[0]-1][i[1]-1] = 1
            if flag2:    
                board[i[0]+1][i[1]-1] = 1
                
        if i[1]+1 < n:
            board[i[0]][i[1]+1] = 1
            if flag1:    
                board[i[0]-1][i[1]+1] = 1
            if flag2:
                board[i[0]+1][i[1]+1] = 1
    
    count = 0
    for i in board:
        for v in i:
            if v==0:
                count += 1
    answer = count
    return answer