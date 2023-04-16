def solution(sizes):
    x,y = 0, 0
    for i,v in sizes:
        x = max(x, max(i,v))
        y = max(y, min(i,v))
    print(x,y)
    answer = x*y
    return answer