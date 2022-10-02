def solution(s, n):
    num1='abcdefghijklmnopqrstuvwxyz'
    num2=num1.upper()
    answer=''
    
    for i in s:
        if i in num1:
            answer+=num1[(num1.find(i)+n)%26]
            
        elif i in num2:
            if i in num2:
                answer+=num2[(num2.find(i)+n)%26]
                
        else:
            answer+=i
            
    return answer