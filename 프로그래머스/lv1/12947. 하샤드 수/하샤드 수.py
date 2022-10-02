def solution(x):
    num=list(map(int,str(x)))
    a=sum(num)
    
    if x%int(a)==0:
        return True
    else:
        return False