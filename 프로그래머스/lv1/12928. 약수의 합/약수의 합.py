def solution(n):
    sum=0
    for num in list(range(1,n+1)):
        if n%num==0:
            sum+=num
    
    answer = sum
    return answer