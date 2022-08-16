N, M, K, X = map(int, input().split())

array = [[1e9] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    array[a - 1][b - 1] = 1

for i in range(N):
    array[i][i] = 0

visited = [False] * N
visited[X - 1] = True
distance = (array[X - 1])

for i in range(N):
    min_ = int(1e9)
    index = 0

    for j in range(N):
        if not visited[j] and distance[j] < min_:
            min_ = distance[j]
            index = j
            if index == 0:
                break

        visited[index] = True
        for k in range(N):
            if not visited[k]:
                if distance[index] + array[index][k] < distance[k]:
                    distance[k] = distance[index] + array[index][k]

check = False
for i in range(N):
    if distance[i] == K:
        print(i + 1)
        check = True
if check == False:
    print(-1)

# N = 4
# M = 4
# K = 2
# X = 1
# a,b = [1, 2]
# a,b = [1, 3]
# a,b = [2, 3]
# a,b = [2, 4]