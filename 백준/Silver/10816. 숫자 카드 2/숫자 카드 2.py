import sys
N = int(input())
number_list = list(map(int, input().split()))
answer = {}
for i in number_list:
    if i not in answer:
        answer[i] = 1
    else:
        answer[i] += 1
        
M = int(input())
number_list = list(map(int,input().split()))
for v in number_list:
    if v in answer:
        print(answer[v], end = ' ')
    else:
        print(0, end = ' ')