
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
def solution(babbling):
    answer = 0

    for word in babbling:
        while word:
            if word[:2] in ["ye","ma"]:
                if word[:2] == word [2:4]:
                    break
                word = word[2:]
                if len(word) == 0:
                    answer +=1
                    continue
            elif word[:3] in ["aya", "woo"]:
                if word[:3] == word [3:6]:
                    break
                word = word[3:]
                if len(word) == 0:
                    answer +=1
                    continue
            else:
                break
    return answer
