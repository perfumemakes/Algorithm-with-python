import sys
n = map(int, sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr = sorted(arr)
result = 0

for i in range(0,len(arr)):
    result += sum(arr[0:i+1])
    
print(result)