def solution(arr):
    sum=0
    for v in arr:
        sum+=v
        
    answer = sum/len(arr)
    return answer