def solution(dots):
    dot = sorted(dots)
    answer = (dot[1][1] - dot[0][1]) * (dot[2][0] - dot[0][0])
    return answer