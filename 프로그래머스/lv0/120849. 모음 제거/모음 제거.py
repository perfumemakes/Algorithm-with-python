def solution(my_string):
    answer = []
    for i in my_string:
        if i not in ["a", "e", "i", "o", "u"]:
            answer.append(i)
    answer = "".join(answer)
    
    return answer