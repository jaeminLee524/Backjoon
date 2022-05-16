# 각 자릿수의 합
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  # while x > 0:
  #   sum += x%10
  #   x = x//10
  for i in str(x): # 문자열로 변환해서 사용
    sum+=int(i)
    
  return sum

max = -2147000000
for x in a:
  total = digit_sum(x)
  if total > max:
    max = total
    response = x

print(response) 
