def solution(numbers, k):
    n = len(numbers)
    m = k*2 -1
    answer = numbers[m%n-1]
    return answer