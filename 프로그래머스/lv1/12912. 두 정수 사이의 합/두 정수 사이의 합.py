def solution(a, b):
    if (a<b):
        sum=0
        while(a<b+1):
            sum += a
            a += 1
        return sum
    else :
        sum=0
        while(b<a+1):
            sum += b
            b += 1
        return sum
    
    print(solution)