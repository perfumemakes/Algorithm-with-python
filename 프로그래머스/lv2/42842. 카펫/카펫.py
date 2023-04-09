def solution(brown, yellow):
    block = brown + yellow
    answer = []
    
    for i in range(3, int(block**0.5) +1):
        if block % i != 0:
            continue
        m = block//i
        
        if (m-2)*(i-2) == yellow:
            answer.append(m)
            answer.append(i)
            break
    return answer