def solution(p):
    if p == "":
        return p
    
    cnt, idx = 0, 0
    for i in range(len(p)):
        if p[i] == "(" :
            cnt += 1
        else :
            cnt -= 1
            
        if cnt == 0 :
            idx = i
            break
    u, v = p[:idx+1], p[idx+1:]
    
    if u[0] == "(":
        return u + solution(v)
    
    else:
        new_u = ""
        for i in u[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("
        
        return "(" + solution(v) +")" + new_u