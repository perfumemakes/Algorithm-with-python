dartResult="1S2D*3T"

def solution(dartResult):
    
    arr = []
    dartResult = dartResult.replace("10", "P")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i.isdigit() or i=='A':
            arr.append(10 if i == 'P' else int(i))
        elif i in ('S', 'D', 'T'):
            num = arr.pop()
            arr.append(num ** bonus[i])
        elif i == '#':
            arr[-1] *= -1
        elif i == '*':
            num = arr.pop()
            if len(arr):
                arr[-1] *= 2
            arr.append(2 * num)
    return sum(arr)

print(solution(dartResult))
