"""
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
"""

'''
# for문 이용

for i in range(1,4):
    for j in range(1,4):
        if i==j:
            continue
        for k in range(1,4):
            if i==k or j==k:
                continue
            print(i,j,k, end=' / ')

'''


'''
visited=[0]*len(range(1,5)) #visited=0 사용 가능, visited=1 사용 불가
arr=[0]*3

for i in range(1,4):
    visited[i]=1
    arr[0]=i
    for j in range(1,4):
        if visited[j]:
            continue
        visited[j]=1
        arr[1]=j
        for k in range(1,4):
            if visited[k]:
                continue
            visited[k]=1
            arr[2]=k
            print(arr)
            visited[k]=0
        visited[j]=0
    visited[i]=0 

print(arr)
'''

# 재귀 함수 이용
arr=[1, 2, 3]
len=len(arr)
visited=[0]*len
answer=[]

def permutation(num): 
    if num >= len: #재귀문 종료 조건
        print(answer)
        return 
    
    for i in range(len): 
        if visited[i]:continue
        visited[i]=1
        answer.append(arr[i])

        permutation(num+1) #재귀문
        visited[i]=0
        answer.pop()
        

permutation(0)

