'''
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
'''
import sys
sys.setrecursionlimit(2000)

def find(chk, rooms):
    if chk not in rooms:
        rooms[chk]=chk+1
        return chk
    empty = find(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty
    
def solution(k, room_number):
    rooms = dict()
    for i in room_number:
        find(i, rooms)
    return list(rooms)
        