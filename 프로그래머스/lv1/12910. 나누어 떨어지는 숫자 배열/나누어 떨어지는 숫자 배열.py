def solution(arr, divisor):
    
    answer = sorted([v for v in arr if v%divisor==0])
    
    if answer==[]:
        return [-1]
    else: return answer