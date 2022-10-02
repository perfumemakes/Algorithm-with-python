def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    arr1=[]
    arr2=[]
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i] + str2[i+1])

    inter = set(arr1) & set(arr2)
    uni = set(arr1) | set(arr2)

    sum_inter = sum([min(arr1.count(word), arr2.count(word)) for word in inter])
    sum_uni = sum([max(arr1.count(word), arr2.count(word)) for word in uni])

    if sum_uni==0:
        answer = 65536
        return answer
        
    answer = int((sum_inter/sum_uni)*65536)

    return answer