from collections import deque

adj = [[0] * 13 for _ in range(13)]


def bfs():
    dq = deque()
    dq.appned(0)  # 초기 루트 값

    while dq:
        now = deque.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                deque.append(nxt)

bfs()