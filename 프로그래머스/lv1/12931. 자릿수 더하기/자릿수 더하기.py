def solution(n):
    sum=0
    str_num = str(n)
    
    for i in str_num:
        sum += int(i)
        
    return sum