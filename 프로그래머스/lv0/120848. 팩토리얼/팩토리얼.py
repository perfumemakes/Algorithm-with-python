def solution(n):
    i = 1
    v = 1
    while i < n:
        v+=1
        i*=v
        if i > n:
            return v-1
                    
    answer = v
    return answer