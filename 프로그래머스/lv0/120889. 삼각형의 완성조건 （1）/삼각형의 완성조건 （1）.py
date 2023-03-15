def solution(sides):
    sides = sorted(sides)
    mnum = sides[2]
    onum = sides[0] + sides[1]
    if mnum < onum:
        return 1
    else:
        return 2