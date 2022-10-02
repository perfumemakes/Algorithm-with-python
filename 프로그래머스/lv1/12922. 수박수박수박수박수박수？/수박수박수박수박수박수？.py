def solution(n):
    if n!=0:
        if n%2==0:
            answer='수박'*(n//2)
        if n%2!=0:
            answer='수박'*(n//2)+'수'
        
    else :
        answer="양의 정수를 입력하세요"
        
    return answer