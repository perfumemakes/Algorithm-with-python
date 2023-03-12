def gcd(x,y):
    while y:
        x, y = y, (x%y)
    return x
    
def solution(numer1, denom1, numer2, denom2):
            
    numer1 = numer1 * denom2
    numer2 = numer2 * denom1
    
    numer = numer1 + numer2
    denom = denom1 * denom2
    
    x = max(numer, denom)
    y = min(numer, denom)
    
    num = gcd(x, y)
    
    answer = [numer/num, denom/num]
    
    return answer