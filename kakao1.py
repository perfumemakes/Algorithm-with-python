moves=[1, 5, 3, 5, 1, 2 , 1, 4]

board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]


def solution(board, moves):
    from collections import deque

    moves = deque(moves)
    bucket = []
    cnt = 0

    while(moves):
        num = moves.popleft()
        
        for i in range(len(board)):
            doll = board[i][num-1]

            if doll != 0:
                board[i][num-1] = 0

                if bucket and bucket[-1] == doll:
                    bucket.pop()
                    cnt += 2
                else:
                    bucket.append(doll)
                break;
    print(cnt)

solution(board, moves)