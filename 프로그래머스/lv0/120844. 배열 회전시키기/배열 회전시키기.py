def solution(numbers, direction):
    if direction == "right":
        numb = numbers.pop()
        numbers.insert(0, numb)
    else:
        numb = numbers.pop(0)
        numbers.append(numb)

    return numbers