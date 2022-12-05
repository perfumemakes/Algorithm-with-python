import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = [ list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    arr1[i]-=sum(arr2[i])
    
answer = []
    
for i in range(N+M):
    for j in range(N):
        if i<N:
            arr1[i]+=arr2[j][i]
        else:
            arr1.append(0)
            arr1[i]+=arr2[j][i]
    answer.append(arr1[i])
            
for i in answer:
    print(i)