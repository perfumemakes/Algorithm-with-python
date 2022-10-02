def solution(phone_number):
    import re

    p=re.compile(r'\d(?=\d{4})')
    result=p.sub('*', phone_number)
    
    return result