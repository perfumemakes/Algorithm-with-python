def solution(s):
    if s[0] == ")" or s[-1]=="(":
        return False
    else:
        c1, c2 = 0, 0
        a1=[]
        a2=[]
        for i in range(0, len(s)):
            if s[i] == "(":
                c1 +=1
                a1.append(i)
            else:
                c2 +=1
                a2.append(i)
        if c1 != c2:
            return False
        
        for i in range(0, len(a1)):
            if a1[i] > a2[i]:
                return False
        
    return True