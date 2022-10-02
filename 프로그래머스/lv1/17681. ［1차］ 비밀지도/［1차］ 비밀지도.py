def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        new=str(format(arr1[i]|arr2[i], 'b'))
        new=new.rjust(n,'0')
        new=new.replace('1', '#')
        new=new.replace('0', ' ')
        answer.append(new)
    
    return answer