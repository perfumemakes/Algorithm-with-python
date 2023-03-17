def solution(hp):
    first = hp//5
    hp = hp%5
    second = hp//3
    hp = hp%3
    answer = first + second + hp
    return answer