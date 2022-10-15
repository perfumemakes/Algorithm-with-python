import sys 

s = set()
m = int(input())
all = set(str(x) for x in range(1,21))

for i in range(m):
    arr = sys.stdin.readline().rstrip()
    if ' ' in arr:
        command,num = arr.split()
    else: command = arr    
    
    # 문제에 제시된 연산    
    if command == 'add':
        if num in s: continue
        else: s.add (num)
    elif command == 'remove':
        s.discard(num)
    elif command == 'check':
        if num in s:
            print(1)
        else: print(0)
    elif command == 'toggle':
        if num in s:
            s.remove(num)
        else: s.add(num)
    elif command == 'all':
        s = all
    else: s = set()
    