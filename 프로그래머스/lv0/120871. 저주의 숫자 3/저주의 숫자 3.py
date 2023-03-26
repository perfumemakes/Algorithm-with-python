def solution(n):
    #1,2,4,5,7,8,10,11,14,16,17,19,20,22,25
    m = 1
    numbers = []
    while len(numbers)<=100: 
        if '3' in list(str(m)) or m%3==0:
            m+=1
            continue
        numbers.append(m)
        m+=1
    answer = numbers[n-1]
    return answer