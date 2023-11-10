## DFS는 스택 or 재귀로 구현 가능, 보통 재귀로 구현
adj = [[0] * 13 for _ in range(13)]

for row in adj:
    print(row)


def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)

dfs(0)
