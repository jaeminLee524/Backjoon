s = set()
s.add(10)
s.add(20)
s.add(10)
s.add(40)
s.add(50)
print(s)

s.pop() # 어떤 값이 빠졌는지는 알 수 없다. 의미 없다
print(s)

s.remove(50) # 특정 값을 제거한다.
print(s)

s.clear()
print(s)
