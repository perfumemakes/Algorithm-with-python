def solution(p, s):
    import math
    day=[]
    for i in range(len(p)):
        day.append(math.ceil((100-p[i])/s[i]))
        
    time=day[0]
    answer=[]
    num=1
    
    for i in range(1, len(day)):
        if time>=day[i]:
            num+=1
        else:
            answer.append(num)
            num=1 
            time=day[i] 

    answer.append(num)
    
    return answer