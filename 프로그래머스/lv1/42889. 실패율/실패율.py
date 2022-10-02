def solution(N, stages):
    result = {}
    denominator = len(stages)
    for i in range(1, N+1):
        if denominator !=0:
            count = stages.count(i)
            result[i] = count/denominator
            denominator -= count
        else:
            result[i] = 0
    return sorted(result, key=lambda x:result[x], reverse=True)