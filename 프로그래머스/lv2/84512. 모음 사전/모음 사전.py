def solution(word):
    lists = []
    makewords(lists, '', 0)
    answer = lists.index(word) +1
    return answer

def makewords(lists, word, i):
    if i == 6:
        return
    if word != '':
        lists.append(word)
    for n in ['A', 'E', 'I', 'O', 'U']:
        makewords(lists, ''.join([word, n]), i+1)
   