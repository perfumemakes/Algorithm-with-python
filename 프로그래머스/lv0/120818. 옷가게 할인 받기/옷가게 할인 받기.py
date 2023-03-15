def solution(price):
    
    if 100000 <= price < 300000:
        price = int(0.95*price)
        return price
    elif 300000<=price<500000:
        price = int(0.9*price)
        return price
    elif 500000<=price:
        price = int(0.8*price)
        return price
    return price
    