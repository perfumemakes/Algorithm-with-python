def solution(box, n):
    num = 1
    for i in box:
        num*=(i//n)
    answer = num
    return answer