def solution(n):
    num=list(map(int,str(n)))
    num1=sorted(num,reverse=True)
    num2=list(map(str,num1))
    
    sum=''
    for i in num2:
        sum+=i
    answer=int(sum)
    
    return answer