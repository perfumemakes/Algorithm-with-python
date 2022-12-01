def solution(survey, choices):
    ref1 = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    ref2 = {'1':3,'2':2,'3':1,'4':0,'5':1,'6':2,'7':3}
    
    answer = ""
    
    for i in range(len(choices)):
        if choices[i]<4:
            ref1[survey[i][:1]] += ref2[str(choices[i])]
        elif choices[i]>4:
            ref1[survey[i][1:]] += ref2[str(choices[i])]
            
        else:
            continue
            
    if ref1['R']>=ref1['T']:
        answer+=('R')
    else:
        answer+=('T')
        
    if ref1['C']>=ref1['F']:
        answer+=('C')
    else:
        answer+=('F')
        
    if ref1['J']>=ref1['M']:
        answer+=('J')
    else:
        answer+=('M')
        
    if ref1['A']>=ref1['N']:
        answer+=('A')
    else:
        answer+=('N')
    
    return answer