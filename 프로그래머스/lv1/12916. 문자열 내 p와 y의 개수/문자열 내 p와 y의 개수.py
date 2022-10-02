def solution(s):
    
    num1=s.count('p')+s.count('P')
    num2=s.count('y')+s.count('Y')
    
    if num1==num2:
        return True
    else:
        return False