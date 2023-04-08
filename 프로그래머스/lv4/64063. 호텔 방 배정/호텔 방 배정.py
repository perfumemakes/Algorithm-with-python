def solution(k, room_number):
    rooms = {}
    answer = []
    
    for i in room_number:
        n = i
        visit = [n]
        
        while n in rooms:
            n = rooms[n]
            visit.append(n)
            
        answer.append(n)
        for v in visit:
            rooms[v] = n+1
    return answer