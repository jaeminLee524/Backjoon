"""
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
24 18

6
72
"""

firstNum, secondNum = map(int, input().split(" "))
limitNum = min(firstNum, secondNum)
divideNum = [i for i in range(2, limitNum+1)]

index = 0
quo = 1
while index+1 < limitNum:
    division = divideNum[index]
    if firstNum % division == 0 and secondNum % division == 0:
        quo *= division
        firstNum = firstNum // division
        secondNum = secondNum // division
        index = 0
    elif index == limitNum:
        break
    else:
        index+=1

print(quo, quo*firstNum*secondNum, sep='\n')


# 유클리드 알고리즘 이용
# 최대 공약수는 유클리드 알고리즘을 이용해 도출
# 최대 공약수는 a * b 를 최대 공약수로 나눈
a, b = map(int, input().split(" "))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(a, b), a * b // gcd(a, b))