def solution(answers):
    
    count=[0,0,0]
    arr1=[1,2,3,4,5]
    arr2=[2,1,2,3,2,4,2,5]
    arr3=[3,3,1,1,2,2,4,4,5,5]
    
    for num, value in enumerate(answers):
        if value==arr1[num%5]:
            count[0]+=1
        if value==arr2[num%8]:
            count[1]+=1
        if value==arr3[num%10]:
            count[2]+=1
            
    max_count=max(count[0], count[1], count[2])
    answer=[]
    
    for i in range(3):
        if count[i]==max_count:
            answer.append(i+1)
    

        
    return answer