import sys

input = sys.stdin.readline

t = int(input())
numbs = list(map(int, input().split()))
plus, sub, mul, quot = map(int, input().split())

m = -1e9
n = 1e9

def dfs(i, c):

    global plus, sub, mul, quot, m, n

    if i == t:
        m = max(m, c)
        n = min(n, c)

    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, c + numbs[i])
            plus += 1

        if sub > 0:
            sub -= 1
            dfs(i + 1, c - numbs[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i + 1, c * numbs[i])
            mul += 1

        if quot > 0:
            quot -= 1
            dfs(i + 1, int(c / numbs[i]))
            quot += 1


dfs(1, numbs[0])
print(m)
print(n)