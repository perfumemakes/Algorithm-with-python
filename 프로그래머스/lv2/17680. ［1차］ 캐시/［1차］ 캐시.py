def solution(cacheSize, cities):
    
    if cacheSize==0:
        answer = 5*len(cities)
        return  answer
    cache = []    
    answer = 0
    
    for i in cities:
        i = i.lower()
        if i not in cache:
            if len(cache) <cacheSize:
                cache.append(i)
                answer+=5
            else:
                cache.pop(0)
                cache.append(i)
                answer+=5
                
        else:
            cache.pop(cache.index(i))
            cache.append(i)
            answer+=1
            
    return answer