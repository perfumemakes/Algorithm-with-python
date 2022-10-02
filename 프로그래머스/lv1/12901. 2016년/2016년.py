def solution(a, b):
    arr1=[31,29,31,30,31,30,31,31,30,31,30,31]
    arr2=['FRI','SAT','SUN','MON','TUE','WED','THU']

    answer = arr2[(sum(arr1[:a-1])+b-1)%7]
    return answer