def solution(score):
    result = []
    for i in score:
        result.append(sum(i)/2)
    
    answer = []
    sort_result = sorted(result, reverse=True)
    for i in result:
        answer.append(sort_result.index(i)+1)
    print(answer)
    return answer