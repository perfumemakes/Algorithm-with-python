def solution(M, N):
    num1 = min(M,N)
    num2 = max(M,N)
      
    answer = ((num1 / 1) - 1) +(num1 * (num2/1-1))
    return answer