def solution(s):
    
    a=len(s)//2
    
    if len(s) == 1:
        return s

    if len(s) % 2 == 1:
        return s[a:a+1]

    if len(s) % 2 == 0:
        return s[a-1:a+1]