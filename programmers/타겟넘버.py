def solution(numbers, target):
    answer = 0
    dp=[set()]*20
    dp[0].add(numbers[0])
    dp[0].add(-numbers[0])
    for i in (1,len(numbers)):
        dp[i]


    return dp

print(solution([1, 1, 1, 1, 1],3))