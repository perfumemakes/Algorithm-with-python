def solution(keymap, targets):
    
    dict = {}
    answer = []
    for i in keymap:
        temp = list(i)
        for i in temp:
            if i in dict:
                dict[i] = min(dict[i], temp.index(i)+1)
            else:
                dict[i] = temp.index(i)+1
    
    for keywords in targets:
        count = 0
        for char in keywords:
            if (char in dict):
                count += dict[char]
            else:
                count = -1
                break
        answer.append(count)

    print(answer)
    return answer