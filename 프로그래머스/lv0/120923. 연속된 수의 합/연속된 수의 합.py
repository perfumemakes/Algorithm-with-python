def solution(num, total):
    
    d = (num)*(num-1) // 2    
    snumb = (total-d)//num
    answer = [i for i in range(snumb, snumb+num)]
    return answer