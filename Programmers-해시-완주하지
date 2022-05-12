# 단순 loop문
# def solution(participant, completion):
#     answer = ''
#     sp = sorted(participant)
#     sc = sorted(completion)
    
#     # 정렬한 참가자, 완주자를 비교, 다를 경우 해당 참가자 return
#     for i in range(len(sc)):
#         if sp[i] != sc[i]:
#             return sp[i]
    
#     # 완주자 모두 참가한 경우에는 정렬했기에 가장 마지막 참가자 return
#     return sp[len(sp)-1]

# Hash 이용
# def solution(participant, completion):
#     hashDict = {}
#     hashSum = 0
    
#     # Dictionary에 참가자 {해쉬값, 이름} 삽입
#     for part in participant:
#         hashDict[hash(part)] = part
#         hashSum += hash(part)
    
#     # 완주자의 해쉬값을 hashSum에서 뺌
#     for comp in completion:
#         hashSum -= hash(comp)
# Dictionary에 남은 참가자 = 완주하지 못한 자
    # return hashDict[hashSum]
        
# Counter 객체 이용        
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
		return list(answer.keys())[0]	
