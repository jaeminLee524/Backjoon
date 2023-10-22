# loop 이용 -> 효율성 테스트케이스 2/4 시간초과
# def solution(phone_book):
    
#     # 두놈씩 비교
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True

# 정렬과 루프 이용
# def solution(phone_book):
#     phone_book.sort()
    
#     # 두놈씩 비교 (단방향)
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
#     return True
    
#     # 두놈씩 비교 (단방향)
#     for first, second in zip(phone_book, phone_book[1:]):
#         if second.startswith(first):
#             return False
#         return True

# 해시 이용
def solution(phone_book):
    hashMap = {}
    for phone_number in phone_book:
        hashMap[phone_number] = 1
    
    for phone_number in phone_book:
        jubdoo = ""
        for phone in phone_number:
            jubdoo += phone
            if jubdoo in hashMap and jubdoo != phone_number:
                return False
    return True
