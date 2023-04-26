def solution(number, limit, power):
    answer = 0
    arr = [1]* (number+1) # 모든수는 1을 약수로가짐
    for i in range(2,number+1): # 2부터시작해서
        for j in range(i,number+1,i): # 해당수의 배수는 전부 1증가
            arr[j]+=1
    
    for i in range(1,len(arr)):
        if arr[i]>limit:
            answer+=power
        else:
            answer+=arr[i]
    return answer

# 시간초과
# def solution(number, limit, power):
#     answer = 0
#     arr= []
#     for i in range(1,number+1):
#         num = 0
#         for j in range(1,i+1):
#             if i%j==0:
#                 num+=1
#                 if num>limit:
#                     answer+=power
#                     break
#         else:
#             answer+=num

#     return answer

print(solution(10,3,2))

# 만약 limit이 1일때도 생각해야함

# 일단 약수의 갯수를 구하고 limit이 넘으면 power를 append, 안넘으면 갯수를 append
# 숫자가 주어졌을 때 약수의 갯수를 빠르게 구하는 방법
# 범위는 1부터 n//2까지만 확인하면됨