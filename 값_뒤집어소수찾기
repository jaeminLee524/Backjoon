# 입력받은 값 중 뒤집은 값이 소수인 숫자를 구하기
# 값 뒤집기 func
def reverse(x):
  res = 0
  while x > 0:
    t = x%10
    res = res * 10 + t
    x = x//10

  return res
  
# 소수 검증 func
def isPrime(x):
  if x == 1:
    return False
  for i in range(2, (x//2)+1):
    if x%i==0: # 약수 존재시 False
      return False
  else: # for문 정상 종료 후
    return True
    
a = list(map(int, input().split(' ')))

for x in a:
  # x 뒤집기
  reversedX = reverse(x)
  if isPrime(reversedX):
    print(reversedX)
