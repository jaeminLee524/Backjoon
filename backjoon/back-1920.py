# 특정 정수의 등장 여부만 체크
# Python에서는 dictionary 자료형을 해시처럼 사용 가능
# set 자료형을 이용 가능
# set : 중복 불가능한 집합
N = int(input())
array_A = set(map(int, input().split())) # 최초 입력받는건 중복X [3,5,7] => {3,5,7}
M = int(input())
list_B = list(map(int, input().split()))

for i in list_B:
    if i not in array_A:
        print('0')
    else:
        print('1')

#
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5