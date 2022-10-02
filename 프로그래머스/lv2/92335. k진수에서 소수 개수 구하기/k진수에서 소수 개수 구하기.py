import string

tmp = string.digits+string.ascii_lowercase

def convert(num, k):
    q, r = divmod(num,k)
    
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) +tmp[r]
    
def is_prime(num):
    if num == 2 or num ==3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num ** 0.5)+1, 2):
        if num % i == 0 :
            return False
    return True
    
def solution(n, k):
    answer = 0
    numbers = convert(n,k)
    
    for i in numbers.split('0'):
        if i == "":
            continue
        if is_prime(int(i)):
            answer +=1
            
    return answer