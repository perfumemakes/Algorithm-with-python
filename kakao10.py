def solution(m, n, board):

    for i in range(m):
        board[i] = list(board[i])

    cnt = 0
    numbers = set()

    while True:
        for i in range(m-1):
            for j in range(n-1):
                hit = board[i][j]
                if hit == []:
                    continue
                if board[i+1][j] == hit and board[i][j+1] == hit and board[i+1][j+1] == hit:
                    numbers.add((i, j))
                    numbers.add((i+1, j))
                    numbers.add((i, j+1))
                    numbers.add((i+1, j+1))
        if numbers:
            cnt += len(numbers)
            for i, j in numbers:
                board[i][j] = []
                numbers = set()
        else:
            return cnt

        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
