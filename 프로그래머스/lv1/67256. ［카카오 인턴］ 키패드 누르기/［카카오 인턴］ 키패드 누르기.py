def solution(numbers, hand):
    board = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]

    result = []
    l_position = board[10]
    r_position = board[11]

    for i in numbers:
        if i in [1, 4, 7]:
            result.append("L")
            l_position = board[i]
        elif i in [3, 6, 9]:
            result.append("R")
            r_position = board[i]

        else:
            if abs(l_position[0] - board[i][0]) + abs(l_position[1] - board[i][1]) > abs(r_position[0] - board[i][0]) + abs(r_position[1] - board[i][1]):
                result.append("R")
                r_position = board[i]
            elif abs(l_position[0] - board[i][0]) + abs(l_position[1] - board[i][1]) < abs(r_position[0] - board[i][0]) + abs(r_position[1] - board[i][1]):
                result.append("L")
                l_position = board[i]
            else:
                result.append(hand[:1].upper())

                if hand[:1] == "r":
                    r_position = board[i]
                else:
                    l_position = board[i]

    result = "".join(result)
    print(result)
    return result