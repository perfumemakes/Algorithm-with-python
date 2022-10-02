def solution(numbers, target):
    
    start=[0]
    for i in numbers:
        end=[]
        for j in start:
            end.append(j+i)
            end.append(j-i)
            start=end
    return start.count(target)