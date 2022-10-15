import sys
import heapq

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

INF = int(1e9)
distance = [INF] * (n + 1)

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(x)

check = False

for i in range(1, n + 1):
    if distance[i] == k:
        check = True
        print(i)

if check == False:
    print(-1)
    