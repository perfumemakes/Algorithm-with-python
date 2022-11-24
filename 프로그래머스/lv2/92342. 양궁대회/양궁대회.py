from collections import deque

def bfs(n, info):
    res = []
    q = deque([(0, [0] * 11)])
    maxGap = 0
    
    while q:
        
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion :
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)
        
        elif sum(arrow) > n:
            continue
        
        elif focus == 10:
            temp = arrow.copy()
            temp[focus] = n-sum(temp)
            q.append((-1, temp))
            
        else:
            temp = arrow.copy()
            temp[focus] = info[focus]+1
            q.append((focus+1, temp))
            temp2 = arrow.copy()
            temp2[focus] = 0
            q.append((focus+1, temp2))
    
    print(res)
    return res

def solution(n, info):
    win_list = bfs(n, info)
    
    if not win_list:
        return [-1]
    elif len(win_list) == 1:
        return win_list[0]
    else:
        return win_list[-1]
    