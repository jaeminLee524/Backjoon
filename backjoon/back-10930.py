# hashlib의 sha256 함수를 이용 => SHA256 해시
# hashlib.sha256(문자열 바이트 객체).hexdigest(): 해시 결과 문자열
import sys
import hashlib

input = sys.stdin.readline
encoded_data = input.encode()

result = hashlib.sha256(encoded_data).hexdigest()

print(result)
