def solution(s):
    s = list(s.split())
    answer = []
    
    for i in range(0, len(s)-1):
        if s[i] == "Z" or s[i+1] == "Z":
            continue
        answer.append(int(s[i]))
    
    if s[-1] != "Z":
        answer.append(int(s[-1]))
    result = sum(answer)
    return result