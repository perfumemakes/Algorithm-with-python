def hanoi(n, start, mid, end, answer):
    if n==1:
        #print(f'원판 1을 {start}에서 {end}로 옮긴다')
        return answer.append([start, end])
    hanoi(n-1, start, end, mid, answer)
    #print(f'원판 {n}을 {start}에서 {end}로 옮긴다')
    answer.append([start, end])
    hanoi(n-1, mid, start, end, answer)
    

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

if __name__=="__main__":
    solution(3)