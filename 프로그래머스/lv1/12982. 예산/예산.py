def solution(d, budget):
    
    d.sort() # 원함수 배열 수정
    
    while budget < sum(d):
        d.pop()
    return len(d)