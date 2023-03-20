def solution(my_string):
    new_string = [i for i in my_string if i.isdigit() == True]
    new_string = [int(i) for i in new_string]
    answer = sorted(new_string)
    return answer