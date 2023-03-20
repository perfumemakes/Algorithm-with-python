def solution(my_string):
    my_string=list(dict.fromkeys(my_string))
    answer = ''.join(my_string)
    return answer