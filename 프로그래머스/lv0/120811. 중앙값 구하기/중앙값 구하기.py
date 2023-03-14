def solution(array):
    array = sorted(array)
    num = len(array)//2
    answer = array[num]
    return answer

if __name__=="__main__":
    solution(array)