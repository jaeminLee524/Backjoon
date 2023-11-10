array = [i for i in range(10)]
print(array)

print(1e9)
print(int(1e9))

a = 0.3 + 0.6

if a == 0.9:
    print(True)
    print(a)
else:
    print(False)
    print(a)


print(round(a))

if round(a, 4) == 0.9:
    print(True)
    print(round(a, 4))
else:
    print(False)
    print(round(a, 4))


b = 2.78799


array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

m = 3
n = 4
array = [[0] * m for _ in range(n)]

print("test", array)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]

print(result)

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement


# 모든 순열 구하기
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print("permutataions: ", result)

# 2개를 뽑는 모든 순열 구하기(중복 허용)
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print("product: ", result)

# 2개를 뽑는 모든 조합 구하기
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print("combinations: ", result)

# 2개를 뽑는 모든 조합 구하기(중복 허용)
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print("combinations_with_replacement: ", result)

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print("count blue: ", counter['blue'])
print("count red: ", counter['red'])
print("counter dict: ", dict(counter))

s1 = "this is python string"

print(s1[:])
print(s1[8:])
print(s1[:7])
print(s1[8:14])
print(s1[-6:])
print(s1[:-7])
print(s1[0:len(s1):2])

s2 = "this is python string"

print("index: ", s2.index('i'))
# print(s2.index('x')) # 없으면 ValueError 발생

print("find:", s2.find('i')) # 앞에서부터 탐색, index 반환
print("find:", s2.find('x'))
print("rfind:", s2.rfind('n')) # 뒤에서부터 탐색, index 반환

print("startswith:", s2.startswith('this')) # 특정 문자열로 시작하면 True
print("startswith:", s2.startswith('is')) # 특정 문자열로 시작하면 True
print("endswith:", s2.endswith('this')) # 특정 문자열로 끝나면 True
print("endswith:", s2.endswith('string')) # 특정 문자열로 끝나면 True

s3 = "      this is python string         "

print(s3.strip()) # 공백 지우기
print(s3.lstrip()) # 왼쪽 공백 지우기
print(s3.rstrip()) # 오픈쪽 공백 지우기

s4 = "This Is Python String"
s5 = "this is python string"
print(s4.islower()) # 모두 소문자인지
print(s5.isupper()) # 모두 대문자인지

s6 = "This Is Python String"
print(s6.swapcase()) # 소문자와 대문자를 바꾼 문자열 반환

s6 = "this Is Python String"
print(s6.title()) # 단어의 맨 앞 글자만 대문자로 변환
print(s6.istitle()) # 단어의 맨 앞 글자만 대문자면 True

s7 = "this, is, python, string"
s8 = "this is python string"
print(s7.split(','))
print(s8.split())

s9 = "this is python string"
print(s9.replace('python', 'my'))

s10 = "this is python string string string string"
print(s10.replace('string', 'S', 3))

s11 = ['this', 'is', 'python', 'string']
print("_".join(s11))

s12 = "this is python string123"
print(s12.isalnum()) # isalnum 문자열이 알파벳과 숫자로만 이루어져 있는지

s13 = "thisispythonstring12312321"
print(s13.isalnum())

print(s12.isalpha()) # isalpha 문자열이 알파벳으로만 이루어져 있는지
print(s13.isalpha())

s14 = "1234"
print(s14.isdigit()) # isdigit 문자열이 숫자로만 이루어져 있는지
print(s14.isnumeric()) # isnumeric 문자열이 숫자로만 이루어져 있는지

my_string = "ABCDE"
print(my_string[::-1])

# reverse: 원본 배열을 손상하며, 반환값은 None
my_list = ["A", "B", "C", "D", "E"]
print(my_list.reverse()) # 원본 배열이 손상된다.

# sorted: 원본 배열을 손상하지 않고, 정렬한 새배열을 반환값으로 준다.
my_list2 = ["B", "F", "A", "C", "E"]
print(sorted(my_list2))
print(sorted(my_list2, reverse=True))

## 리스트 컴프리헨션
## if만 쓸거면 for 오른쪽, else까지 쓸거면 for 왼쪽에
print([i for i in range(5)])
print([i*10 for i in range(5)])
print([i for i in range(5) if i%2==0])
print([i if i%2==0 else 'odd' for i in range(5)])
print([(i,j) for i in range(2) for j in range(3)])
print([i if i%2==0 else 'odd-1' if i==1 else 'odd-3' for i in range(5)])

## 인덱스 가져오기
for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)

print("------------------")

## 여러개의 배열 동시에 돌기
for a1, a2 in zip(['a', 'b', 'c'], [1, 2, 3]):
    print(a1, a2)

## 빈배열일때 첫번째 원소 오류없이 가져오기
my_list3 = []
# print(my_list3[0]) # 오류 발생
print(my_list3[-1:])

## 2차원 배열 올바르게 선언하기
arr = [[0 for i in range(2)] for j in range(3)] ## 2: col, 3: row
arr2 = [[0 for i in range(3)] for j in range(4)]
print(arr)
print(arr2)

my_list4 = [1,2,3,4,5]
for i in my_list4[:]: # my_list4[:]로 복사본을 만들어서 루프에 넣는다.
    print(i)
    my_list4.remove(i)
print(my_list4)

my_set = set(['A', 'B', 'C', 'D', 'A', 'A'])
print(my_set)

# 원소 한개 추가하기
my_set2 = {'A', 'B'}
my_set2.add('D')
print(my_set2)

# 원소 여러개 추가하기
my_set3 = {'A', 'B'}
my_set3.update('D', 'E')
print(my_set3)

# 집합은 순서가 없어서 특정값을 인덱스로 불러올 수 없다.
my_set4 = {'A', 'C', 'D', 'B', 'E'}
for s in my_set4:
    print(s)

## 사전(dictionary)
# 값 갱신하기
my_dict = {"A": 1, "B": 2}
my_dict["C"] = 3
print(my_dict)
my_dict["A"] = 0
print(my_dict)

# key 리스트와 value 리스트 모두 가져오기
my_dict2 = {"A": 1, "B": 2, "C": 3}
print(my_dict2.items())

# key 리스트만 가져오기
print(my_dict2.keys())

# value 리스트만 가져오기
print(my_dict2.values())

# 해당 key의 value 가져오기
print(my_dict2["A"])
print(my_dict2.get("A"))
# print(my_dict2["E"]) # 에러
print(my_dict2.get("E")) # 에러 발생 안함

print("---------------------------")

my_dict3 = {"A": 100, "B": 10, "C": 50}
print(sorted(my_dict3, key=lambda x:my_dict3[x]))
print(my_dict3)

# 딕셔너리 key <> value 바꾸기
    # :value로 key를 검색해야하는데, for문으로 검색하면 시간초과가 날때 사용
reversed_dictionary = dict(map(reversed, my_dict3.items()))
print(reversed_dictionary)

print("---------------------------")

## 튜플(tuple)
# 특정 요소 가져오기
my_tuple = (1, 2, 3, 4, 5)
print("tuple: ", my_tuple[2])

# 튜플 내부의 값을 하나씩 쪼개서 가져오기
for a, b in [(1,2), (3,4)]:
    print(a, b)

# 내부의 값을 변경하거나 삭제할 수 없다.
# 하지만, 통째로 변경은 가능하다.

print("---------------------------")

nums = [2,7,11,15]
target = 9

output = []
for i in range(len(nums)):
    i_val = nums[i]
    for j in range(1, len(nums)):
        if i == j:
            break
        j_val = nums[j]
        if i_val + j_val == target:
            output.append(i_val)
            output.append(j_val)
            print(output)
