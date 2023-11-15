import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1

answer = 0
check = [False] * N


def dfs(now):
    for next in range(N):
        if adj[now][next] and not check[next]:
            check[next] = True
            dfs(next)


for i in range(N):
    if not check[i]:
        answer += 1
        check[True]
        dfs(i)

print(answer)
