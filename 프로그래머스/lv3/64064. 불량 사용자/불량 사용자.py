from itertools import permutations
import re

def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*', '.')
    print(banned)
    
    answer = set()
    
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))
    print(answer)
    return len(answer)