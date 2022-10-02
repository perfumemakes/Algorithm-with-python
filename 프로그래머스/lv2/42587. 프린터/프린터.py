def solution(priorities, location):
    loc=[i for i in range(len(priorities))]
    answer=[]
    while(len(priorities)!=0):
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer.append(loc.pop(0))
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            
    return (answer.index(location)+1)