from typing import Dict


def solution(msg):
    d = {x: i+1 for i,x in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    end = 27
    length = len(msg)
    start = 0
    max_len = 1
    answer = []
    while start < length:
        index = max_len
        while True:
            tmp = msg[start:start+index]
            if tmp in d:
                answer.append(d[tmp])
                d[msg[start:start+index+1]] = end
                end += 1; max_len += 1
                break
            index -= 1
        start += index
    return answer

dict = {x: i+1 for i,x in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
print(dict)