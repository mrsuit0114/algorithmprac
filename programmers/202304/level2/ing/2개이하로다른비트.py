

# 시간초과 count를 좀 풀어서 해봤는데 그래도 시간초과나네
def solution(numbers):
    answer = []
    for num in numbers:
        tmp = num+1
        while(True):
            bit = 0
            for i in bin(tmp^num)[2:]:
                if i =='1': # 서로다른 비트면
                    bit+=1
                    if bit>2:
                        break
            else:
                answer.append(tmp)
                break
            tmp+=1
        
    return answer

print(solution([2,7]))



# 2개면 2개지 2개 이하는 머냐
# number를 비트로 나타내고 +1씩하고 두 수를 xor(다르면 1) 1이 2개 이하인 수 리턴
