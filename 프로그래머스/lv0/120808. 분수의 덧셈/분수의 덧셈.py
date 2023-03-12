def gcd(x,y):
    while y:
        x, y = y, (x%y)
    return x
    
def solution(numer1, denom1, numer2, denom2):
    
    for i in range(max(denom1, denom2), denom1*denom2 +1):
        if i % denom1 == 0 and i % denom2 == 0:
            target = i
            break
            
    numer1 = numer1 * (target//denom1)
    numer2 = numer2 * (target//denom2)
    
    numer = numer1 + numer2
    denom = target
    
    x = max(numer, denom)
    y = min(numer, denom)
    
    num = gcd(x, y)
    
    answer = [numer/num, denom/num]
    
    return answer