def solution(num_list, n):
    len_num_list = len(num_list)
    answer = []
    m=0
    while len(answer) != len_num_list//n:
        answer.append(num_list[m:m+n])
        m+=n
    return answer