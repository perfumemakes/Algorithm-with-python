# n=1380

# a = 1380//500
# b = (1380 - 500*a)//100
# c = (1380 - 500*a - 100*b)//50
# d = (1380 - 500*a - 100*b - 50*c)//10

# answer = a+b+c+d
# print(answer)
# print(a,b,c,d)

# coins = [500, 100, 50, 10]
# count = 0
# for i in coins:
#     count += n//i
#     n = n%i
# print(count)

def function():
    n,m,k = map(int, input().split())
    data = list(map(int, input().split()))
    
    data.sort()
    first =data[n-1]
    second = data[n-2]
    result = 0
    
    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1

            
        if m == 0:
            break
        result += second
        m -= 1       
    
    print(result)

def function2():
    n,m,k=map(int, input().split())
    data=list(map(int, input().split()))
    
    data.sort()
    first = data[n-1]
    second = data[n-2]
    result = 0
    num = first*k+second
    
    result = (m//(k+1)*num) + (m%(k+1)*first)
    print(result)

def function3():
    n,m = map(int, input().split())
    count = 0
    while True:
        if(n==1):
            break
        elif(n%m==0):
            n=n//m
            count+=1
        else:
            n=n-1
            count+=1
    print(count)
    
function3()
    