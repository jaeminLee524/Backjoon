s = []
s.append(10)
s.append(20)
s.append(30)
print("size: ", len(s))
print("stack: ", s)

while(len(s) > 0):
    print(s[-1])
    s.pop(-1)