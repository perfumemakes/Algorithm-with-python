def solution(x, n):
    if x>0:
        a=x*n+1
        answer = list(range(x,a,x))
        return answer
    if x<0:
        a=(x*n)-1
        answer = list(range(x,a,x))
        return answer
    if x==0:
        return [0]*n