
from copy import deepcopy

def check_move(board, loc):
    r, c = loc
    for idx, (dr, dc) in enumerate([[0,1], [0, -1],  [1, 0], [-1, 0]]):
        nr, nc = r +dr, c +dc
        if ((0 <= nr < len(board)) and (0 <= nc < len(board[0])) and board[nr][nc] == 1):
            return True
        
    return False

def search(board, aloc, bloc, step):
    r,  c = aloc if step%2 == 0 else bloc
    if check_move(board, [r,c]) == False:
        return (False, 0)
    if aloc==bloc:
        return (True, 1)
    
    nboard = deepcopy(board)
    nboard[r][c] = 0
    flag = False
    max_turn, min_turn = 0, float('inf')
    for idx, (dr, dc) in enumerate([[0,1], [0, -1], [1, 0], [-1, 0]]):
        nr, nc = r + dr, c + dc
        if ((0 <= nr < len(board)) and (0 <= nc < len(board[0])) and board[nr][nc] == 1):
            if step%2 == 0:
                ret = search(nboard, [nr, nc], bloc, step+1)
            else:
                ret = search(nboard, aloc, [nr, nc], step+1)
                
            if ret[0]==False:
                flag = True
                min_turn = min(min_turn, ret[1])
            else:
                max_turn = max(max_turn, ret[1])
                
    if flag == True:
        return (flag, min_turn+1)
    
    else:
        return (flag, max_turn+1)
    
def solution(board, aloc, bloc):
    answer = search(board, aloc, bloc, 0)
    return answer[1]
                