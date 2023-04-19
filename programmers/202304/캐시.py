from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    
    return answer


# 런타임 에러나는 케이스가있는데 못찾겠다 근데 이렇게 배열로 그냥되는 줄 알았으면
# 딕셔러니쓴다고 쇼안했는데 사실 딕셔너리가 더 효율이 좋다고도 말 못하겠긴해

# def solution(cacheSize, cities):
#     answer = 0
#     cache = []
#     dic = {} #캐시에 존재하는지 확인


#     if cacheSize!=0:
#         for city in cities:
#             city = city.upper()
#             if city in dic and dic[city]>=0: # 캐시 히트
#                 idx = dic[city]
#                 for k,v in dic.items():
#                     if 0<=v<idx:
#                         dic[k]+=1
#                 del cache[idx]
#                 cache.insert(0,city)
#                 answer+=1
#             elif city in dic and dic[city]==-1: # 캐시아웃된 경우
#                 tmp = cache.pop() #캐시아웃할 도시
#                 dic[tmp]=-1 # 캐시아웃
#                 for k,v in dic.items():
#                     if v>=0:
#                         dic[k]+=1
#                 cache.insert(0,city)
#                 dic[city] = 0
#                 answer+=5
#             elif city not in dic: #처음나온 도시인 경우
#                 if len(cache)==cacheSize:
#                     tmp = cache.pop()
#                     dic[tmp]=-1
#                     for k,v in dic.items():
#                         if v>=0:
#                             dic[k]+=1
#                     cache.insert(0,city)
#                     dic[city]=0
#                 else:
#                     for k,v in dic.items():
#                         if v>=0:
#                             dic[k]+=1
#                     cache.insert(0,city)
#                     dic[city]=0
#                 answer+=5
#             else:
#                 print("asdfaS?")
#     else:
#         answer = 5*len(cities)
                    

#     return answer

# print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

print(solution(3,["a", "b", "c", "a"]))
print(solution(3,["a", "b", "c", "a", "b"]))
print(solution(3,["a", "b", "c", "a", "b", "d", "c"]))

# dic -> 캐시유무와 인덱스, 없거나 -1이면 캐시에 없음, 0이상이면 캐시에서 인덱스
# 캐시 아웃된 경우, 처음나온 도시인 경우, 캐시에 있는 경우
# 캐시 아웃된 경우 -> 캐시팝한 도시 =-1,모든 키값 순회하면서 0이상인 키값들 +1씩 ,캐시insert(0, city), dic[city]=0 
# 처음 나온 도시인 경우 -> 캐시가 꽉찬 경우 -> 아웃과 동일 , 자리있는 경우 -> 캐시팝 생략하고 아웃과 동일
# 캐시에 있는 경우 -> dic에서 index알아내고 해당 index와 0사이의 값을 가진 키들 +1씩 
# 캐시크기가 0일때 팝하는 상황에서 에러
# 대소문자 구분없는 배열도 나오네

# 가장 오래전에 접근한 데이터를 삭제하고, 추가하는방식 캐시 히트일 경우 순서도 갱신해줘야함
#dic에서 있는지 확인하고 없으면 캐시팝해서 dic에서 처리하고 insert(0,city)하고 dic처리
#각 과정에서 dic처리를 어떻게 할 것이냐
# 캐시에 있다면 value를 1로?

# 어떻게 구현해야 유무는 빠르게 캐치하고 -> dic, 있을 때 캐시를 갱신할 것인가
# 캐시에 없는 경우 -> dic에서 없는 걸 확인하고 캐시에 insert(0,city)
# 캐시에 있는 경우 -> 해당 인덱스를 파악해서 0번 자리로 교체
# 해당 인덱스를 어떻게 파악? -> dic에서 없거나 캐시아웃된경우 키가없거나 값이 -1
# 캐시에 계속 추가되면 인덱스를 계속 밀어줘야하는데
# 추가 됐을 때 dic을 다 돌면서 값이 음수가 아니면 +1을 해줘야함
# 교체 했을 때 0번인덱스를 가진 키값부터 사이에 있는 키들의 값을 1씩 증가후 본인은 0으로



