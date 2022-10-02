def solution(phone_book):
    dic={}
    answer=True
    
    for i in phone_book:
        dic[i]=0
        
    for i in phone_book:
        tmp=''
        for j in i:
            tmp+=j
            if tmp in dic and tmp != i:
                answer = False
    
    return answer