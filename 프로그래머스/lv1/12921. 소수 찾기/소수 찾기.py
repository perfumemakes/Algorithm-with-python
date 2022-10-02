def solution(n):
    arr=[1]*(n+1)
    
    num=int(n**.5)
    for i in range(2, num+1):
        if arr[i]==1:
            for j in range(i*2, n+1, i):
                arr[j] = 0
    
    return len([i for i in range(2, n+1) if arr[i]==1])