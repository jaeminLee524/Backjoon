from collections import deque

q = deque()
q.append(10)
q.append(20)
q.appendleft(0)
print("size: ", len(q))
print("deque: ", q)

while len(q) > 0:
    print(q.popleft())