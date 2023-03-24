def solution(polynomial):
    polynomial = polynomial.replace("+", "")
    polynomial = polynomial.split()
    n1 = 0
    n2 = 0
    for i in polynomial:
        if 'x' in i:
            if len(i) == 1:
                n1 += 1
            else:
                n1 += int(i[:-1]) 
        else:
            n2+=int(i)
            
    if n2 == 0:
        if n1 == 0:
            answer = "0"
        elif n1 == 1:
            answer = "x"
        else:
            answer = f"{n1}x"
    else:
        if n1 == 0:
            answer = f"{n2}"
        elif n1 == 1:
            answer = f"x + {n2}"
        else:
            answer = f"{n1}x + {n2}"
    return answer