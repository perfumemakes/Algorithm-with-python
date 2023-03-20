def solution(my_string):
    new_string = [int(i) for i in my_string if i.isdigit() == True]
    print(new_string)
    answer = sum(new_string)
    return answer