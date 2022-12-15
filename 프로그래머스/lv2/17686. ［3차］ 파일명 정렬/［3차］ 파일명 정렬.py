import re

def solution(files):
    answer = [re.split(r"([0-9]+)", words) for words in files]
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(word) for word in answer]