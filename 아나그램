# 아나그램(Dictionary Hash)
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

list1 = dict()
list2 = dict()

for x in a:
  list1[x] = list1.get(x, 0)+1

for x in b:
  list2[x] = list2.get(x, 0)+1

for i in list1.keys():
  if i in list2.keys():
    if list1[i] != list1[i]:
      print("NO")
      break

  else:
    print("NO")
    break
    
# 정산 출력
else:
  print("YES")
