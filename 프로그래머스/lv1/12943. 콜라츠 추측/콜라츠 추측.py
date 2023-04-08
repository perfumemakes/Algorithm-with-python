def recursion(num, i):
    if num == 1:
        return i
    if i==500:
        return -1
    if num % 2 == 0:
        return recursion(num//2, i+1)
    else:
        return recursion(num*3+1, i+1)

def solution(num):
    return recursion(num, 0)